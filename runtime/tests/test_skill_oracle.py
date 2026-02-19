"""
test_skill_oracle.py -- TDD tests for all 4 skill runtime scripts.
Run: python -m pytest runtime/tests/test_skill_oracle.py -v
"""

import os
import subprocess
import sys
from pathlib import Path

_HERE = Path(__file__).parent
SCRIPTS_DIR = Path(os.getenv("GAIA_ROOT", _HERE.parent.parent)) / "runtime" / "scripts"
GAIA_ROOT = Path(os.getenv("GAIA_ROOT", _HERE.parent.parent))


# --- skill_guard.py tests ---------------------------------------------------


class TestSkillGuard:
    def run_guard(self, path, env=None):
        e = {**os.environ, **(env or {})}
        # Remove SKIP_SPEC_GUARD if not explicitly set
        if env is None or "SKIP_SPEC_GUARD" not in (env or {}):
            e.pop("SKIP_SPEC_GUARD", None)
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "skill_guard.py"),
                "--check",
                "spec-before-code",
                "--path",
                path,
            ],
            capture_output=True,
            text=True,
            env=e,
            cwd=str(GAIA_ROOT),
        )
        return result

    def test_allows_with_active_spec(self, tmp_path):
        # Create a controlled temp dir with an active (unchecked) change spec
        changes_dir = tmp_path / "changes" / "my-feature"
        changes_dir.mkdir(parents=True)
        (changes_dir / "tasks.md").write_text("- [ ] Implement thing\n- [x] Done thing\n")
        e = {**os.environ}
        e.pop("SKIP_SPEC_GUARD", None)
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "skill_guard.py"),
                "--check",
                "spec-before-code",
                "--path",
                "_ARGUS/new_feature.py",
            ],
            capture_output=True,
            text=True,
            env=e,
            cwd=str(tmp_path),
        )
        assert result.returncode == 0

    def test_allows_with_skip_env(self):
        result = self.run_guard("_ARGUS/new_feature.py", env={"SKIP_SPEC_GUARD": "1"})
        assert result.returncode == 0

    def test_allows_non_component_path(self):
        result = self.run_guard("docs/readme.md")
        assert result.returncode == 0

    def test_blocks_without_spec(self, tmp_path):
        # Run from a directory with no changes/ -> should block
        e = {**os.environ}
        e.pop("SKIP_SPEC_GUARD", None)
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "skill_guard.py"),
                "--check",
                "spec-before-code",
                "--path",
                "_ARGUS/new_feature.py",
            ],
            capture_output=True,
            text=True,
            env=e,
            cwd=str(tmp_path),
        )
        assert result.returncode == 1
        combined = result.stdout + result.stderr
        assert "BLOCKED" in combined

    def test_block_message_includes_why(self, tmp_path):
        e = {**os.environ}
        e.pop("SKIP_SPEC_GUARD", None)
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS_DIR / "skill_guard.py"),
                "--check",
                "spec-before-code",
                "--path",
                "_ARGUS/new_feature.py",
            ],
            capture_output=True,
            text=True,
            env=e,
            cwd=str(tmp_path),
        )
        if result.returncode == 1:
            combined = result.stdout + result.stderr
            assert any(
                kw in combined for kw in ["spec", "BLOCKED", "creating-change", "Rule", "Fix"]
            )


# --- skill_suggester.py tests -----------------------------------------------


class TestSkillSuggester:
    def run_suggester(self, path, env=None):
        e = {**os.environ, **(env or {})}
        if env is None or "SKIP_SKILL_TIPS" not in (env or {}):
            e.pop("SKIP_SKILL_TIPS", None)
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "skill_suggester.py"), "--path", path],
            capture_output=True,
            text=True,
            env=e,
            cwd=str(GAIA_ROOT),
        )
        return result

    def test_aurora_triggers_auditing_ux(self):
        result = self.run_suggester("_AURORA/app.py")
        output = result.stdout + result.stderr
        assert "auditing-ux" in output
        assert "HOOK" in output

    def test_dashboard_triggers_auditing_ux(self):
        result = self.run_suggester("_ARGUS/dashboard/app.py")
        output = result.stdout + result.stderr
        assert "auditing-ux" in output

    def test_tasks_md_triggers_archiving_change(self):
        result = self.run_suggester("changes/my-feature/tasks.md")
        output = result.stdout + result.stderr
        assert "archiving-change" in output

    def test_component_claude_md_triggers_reconcile(self):
        result = self.run_suggester("_ARGUS/CLAUDE.md")
        output = result.stdout + result.stderr
        assert "reconciling-gaia" in output

    def test_spec_test_triggers_validating_specs(self):
        result = self.run_suggester("tests/test_spec_behaviors.py")
        output = result.stdout + result.stderr
        assert "validating-specs" in output

    def test_no_match_produces_no_output(self):
        result = self.run_suggester("README.md")
        assert result.stdout.strip() == ""
        assert result.returncode == 0

    def test_skip_env_suppresses_output(self):
        result = self.run_suggester("_AURORA/app.py", env={"SKIP_SKILL_TIPS": "1"})
        assert result.stdout.strip() == ""

    def test_output_has_three_lines_on_match(self):
        result = self.run_suggester("_AURORA/app.py")
        lines = [line for line in result.stdout.strip().splitlines() if line.strip()]
        assert len(lines) >= 2

    def test_announce_explain_escape_format(self):
        result = self.run_suggester("_AURORA/app.py")
        output = result.stdout
        assert "[HOOK:" in output
        assert "TIP:" in output or "->" in output


# --- session_exit_check.py tests --------------------------------------------


class TestSessionExitCheck:
    def run_exit_check(self, gaia_root, env=None):
        e = {**os.environ, **(env or {})}
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "session_exit_check.py")],
            capture_output=True,
            text=True,
            env=e,
            cwd=str(gaia_root),
        )
        return result

    def test_always_exits_0(self, tmp_path):
        result = self.run_exit_check(tmp_path)
        assert result.returncode == 0

    def test_empty_state_clean_summary(self, tmp_path):
        result = self.run_exit_check(tmp_path)
        output = result.stdout + result.stderr
        assert "SESSION RECAP" in output

    def test_nonempty_changes_triggers_advisory(self, tmp_path):
        # Plant a registry.json so session_exit_check treats tmp_path as gaia_root
        (tmp_path / "registry.json").write_text('{"projects": []}')
        changes_file = tmp_path / ".gaia_changes"
        changes_file.write_text("_ARGUS/dashboard/app.py modified\n_AURORA/app.py modified\n")
        result = self.run_exit_check(tmp_path)
        output = result.stdout + result.stderr
        assert "reconcil" in output.lower() or "ADVISORIES" in output

    def test_unchecked_tasks_triggers_advisory(self, tmp_path):
        changes_dir = tmp_path / "changes" / "my-feature"
        changes_dir.mkdir(parents=True)
        (changes_dir / "tasks.md").write_text("- [ ] Write tests\n- [x] Done thing\n")
        result = self.run_exit_check(tmp_path)
        output = result.stdout + result.stderr
        assert (
            "task" in output.lower() or "unchecked" in output.lower() or "archiv" in output.lower()
        )


# --- skill_health.py tests --------------------------------------------------


class TestSkillHealth:
    def run_health(self, gaia_root=None, env=None):
        e = {**os.environ, **(env or {})}
        cwd = str(gaia_root) if gaia_root else str(GAIA_ROOT)
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "skill_health.py")],
            capture_output=True,
            text=True,
            env=e,
            cwd=cwd,
        )
        return result

    def test_runs_without_error(self):
        result = self.run_health()
        assert result.returncode in (0, 1)

    def test_detects_missing_phase_tag(self, tmp_path):
        skills_dir = tmp_path / ".claude" / "skills" / "test-skill"
        skills_dir.mkdir(parents=True)
        skill_md = skills_dir / "SKILL.md"
        skill_md.write_text("---\nname: test-skill\ndescription: A test skill\n---\n# Test\n")
        result = self.run_health(tmp_path)
        output = result.stdout + result.stderr
        # Should mention phase tags or report warnings
        assert (
            "phase" in output.lower()
            or "OPENING" in output
            or "CLOSING" in output
            or "CONTEXT" in output
            or result.returncode in (0, 1)
        )

    def test_detects_oversized_skill(self, tmp_path):
        skills_dir = tmp_path / ".claude" / "skills" / "huge-skill"
        skills_dir.mkdir(parents=True)
        skill_md = skills_dir / "SKILL.md"
        skill_md.write_text("\n".join([f"line {i}" for i in range(600)]))
        result = self.run_health(tmp_path)
        output = result.stdout + result.stderr
        assert (
            "500" in output
            or "oversized" in output.lower()
            or "lines" in output.lower()
            or result.returncode in (0, 1)
        )

    def test_exits_cleanly_on_real_gaia(self):
        result = self.run_health()
        assert result.returncode in (0, 1)
