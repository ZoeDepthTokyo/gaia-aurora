"""
Basic usage example for MNEMIS memory system.

Demonstrates:
- Memory storage across three tiers
- Access control enforcement
- Memory promotion workflow
"""

from mnemis import (
    MnemisStore,
    MemoryAccessController,
    MemoryPromotionEngine,
    MemorySearchEngine,
)
from mnemis.models.memory_models import MemoryAccessLevel


def main():
    """Run basic MNEMIS usage example."""
    print("=== MNEMIS Basic Usage Example ===\n")

    # Initialize components
    store = MnemisStore()
    controller = MemoryAccessController()
    promotion_engine = MemoryPromotionEngine(store, controller)
    search_engine = MemorySearchEngine(store)

    # Example 1: Agent-level ephemeral memory
    print("1. Agent-level ephemeral memory")
    print("-" * 40)

    agent_contract = controller.register_agent(
        agent_id="test_agent",
        access_level=MemoryAccessLevel.AGENT,
        project_id="test_project"
    )

    agent_scope = controller.create_agent_scope(
        agent_id="test_agent",
        project_id="test_project",
        ttl_seconds=3600  # 1 hour
    )

    agent_memory_id = store.write(
        content={"temp_result": "processing..."},
        scope=agent_scope,
        contract=agent_contract,
        tags=["temp", "processing"]
    )

    print(f"Created agent memory: {agent_memory_id}")
    print(f"Auto-expires: Yes (1 hour TTL)\n")

    # Example 2: Project-level persistent memory
    print("2. Project-level persistent memory")
    print("-" * 40)

    project_contract = controller.register_agent(
        agent_id="project_agent",
        access_level=MemoryAccessLevel.PROJECT,
        project_id="test_project"
    )

    project_scope = controller.create_project_scope("test_project")

    project_memory_id = store.write(
        content={
            "pattern": "optimization_technique",
            "description": "Cached LLM responses for repeated queries",
            "performance_gain": "50% cost reduction"
        },
        scope=project_scope,
        contract=project_contract,
        tags=["optimization", "caching"]
    )

    print(f"Created project memory: {project_memory_id}")
    print(f"Persistence: Project lifecycle\n")

    # Example 3: Memory promotion workflow
    print("3. Memory promotion to GAIA tier")
    print("-" * 40)

    proposal_id = promotion_engine.propose_promotion(
        memory_id=project_memory_id,
        to_scope=controller.create_gaia_scope(),
        agent_id="project_agent",
        rationale="This caching pattern is useful for all projects with LLM usage"
    )

    print(f"Promotion proposed: {proposal_id}")

    # Approve promotion
    promoted_memory_id = promotion_engine.approve_promotion(
        proposal_id=proposal_id,
        reviewer="human",
        notes="Approved - excellent cross-project pattern"
    )

    print(f"Promotion approved: {promoted_memory_id}")
    print(f"Memory now accessible to all projects\n")

    # Example 4: Cross-tier memory access
    print("4. Cross-tier memory access")
    print("-" * 40)

    # PROJECT agent can read GAIA memory
    gaia_memory = store.read(promoted_memory_id, project_contract)
    print(f"PROJECT agent reading GAIA memory: {gaia_memory.content['pattern']}")

    # But AGENT cannot read PROJECT memory
    try:
        store.read(project_memory_id, agent_contract)
    except Exception as e:
        print(f"AGENT reading PROJECT memory: BLOCKED ({type(e).__name__})\n")

    # Example 5: Memory search
    print("5. Memory search")
    print("-" * 40)

    # Search by tags
    results = search_engine.search_by_tags(
        tags=["optimization"],
        contract=project_contract,
        match_all=False
    )

    print(f"Search results for 'optimization' tag: {len(results)} memories")
    for memory in results:
        print(f"  - {memory.content.get('pattern', 'N/A')}")

    print("\n=== Example Complete ===")


if __name__ == "__main__":
    main()
