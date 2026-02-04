"""
Basic workflow example for LOOM agent editor.

Demonstrates:
- Agent definition with contracts
- Workflow creation with connections
- Governance rules
- Workflow execution
"""

from loom import (
    AgentNode,
    AgentWorkflow,
    AgentConnection,
    WorkflowEngine,
)
from loom.models.agent_models import (
    AgentType,
    AgentInputSchema,
    AgentOutputSchema,
    GovernanceRule,
)


def main():
    """Run basic LOOM workflow example."""
    print("=== LOOM Basic Workflow Example ===\n")

    # Example 1: Define agents
    print("1. Defining agents")
    print("-" * 40)

    # Data validator agent
    validator = AgentNode(
        id="validator",
        name="Data Validator",
        agent_type=AgentType.TRANSFORMER,
        description="Validates input data structure",
        input_schema=[
            AgentInputSchema(
                name="data",
                type="dict",
                required=True,
                description="Data to validate"
            )
        ],
        output_schema=[
            AgentOutputSchema(
                name="validated_data",
                type="dict",
                description="Validated data",
                confidence_score=True
            )
        ],
        implementation="agents.validate_data"
    )

    # Analyzer agent
    analyzer = AgentNode(
        id="analyzer",
        name="Data Analyzer",
        agent_type=AgentType.EXECUTOR,
        description="Analyzes validated data using LLM",
        input_schema=[
            AgentInputSchema(
                name="validated_data",
                type="dict",
                required=True
            )
        ],
        output_schema=[
            AgentOutputSchema(
                name="analysis",
                type="dict",
                description="Analysis results"
            )
        ],
        implementation="agents.analyze_data",
        governance_rules=[
            GovernanceRule(
                rule_id="cost_limit",
                rule_type="cost_limit",
                constraint={"max_cost": 1.0},
                action_on_violation="halt"
            )
        ]
    )

    # Reporter agent
    reporter = AgentNode(
        id="reporter",
        name="Report Generator",
        agent_type=AgentType.TRANSFORMER,
        description="Generates human-readable report",
        input_schema=[
            AgentInputSchema(
                name="analysis",
                type="dict",
                required=True
            )
        ],
        output_schema=[
            AgentOutputSchema(
                name="report",
                type="str",
                description="Final report"
            )
        ],
        implementation="agents.generate_report"
    )

    print(f"Created 3 agents:")
    print(f"  - {validator.name} (TRANSFORMER)")
    print(f"  - {analyzer.name} (EXECUTOR)")
    print(f"  - {reporter.name} (TRANSFORMER)\n")

    # Example 2: Connect agents
    print("2. Connecting agents")
    print("-" * 40)

    connection1 = AgentConnection(
        id="validator_to_analyzer",
        source_agent_id="validator",
        source_output="validated_data",
        target_agent_id="analyzer",
        target_input="validated_data"
    )

    connection2 = AgentConnection(
        id="analyzer_to_reporter",
        source_agent_id="analyzer",
        source_output="analysis",
        target_agent_id="reporter",
        target_input="analysis"
    )

    print(f"Created 2 connections:")
    print(f"  - validator → analyzer")
    print(f"  - analyzer → reporter\n")

    # Example 3: Create workflow
    print("3. Creating workflow")
    print("-" * 40)

    workflow = AgentWorkflow(
        id="analysis_pipeline",
        name="Data Analysis Pipeline",
        description="Validates, analyzes, and reports on input data",
        agents=[validator, analyzer, reporter],
        connections=[connection1, connection2],
        entry_points=["validator"]
    )

    # Validate workflow
    errors = workflow.validate_workflow()
    if errors:
        print(f"Validation errors: {errors}")
    else:
        print(f"Workflow validated successfully")
        print(f"  - {len(workflow.agents)} agents")
        print(f"  - {len(workflow.connections)} connections")
        print(f"  - Entry point: {workflow.entry_points[0]}\n")

    # Example 4: Register agent implementations
    print("4. Registering agent implementations")
    print("-" * 40)

    def validate_data(inputs):
        """Validate data structure."""
        data = inputs["data"]
        # Simple validation
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary")
        return {
            "validated_data": data,
            "confidence": 1.0
        }

    def analyze_data(inputs):
        """Analyze data using LLM."""
        data = inputs["validated_data"]
        # Mock LLM analysis
        return {
            "analysis": {
                "summary": f"Analyzed {len(data)} fields",
                "insights": ["Data is well-structured", "No anomalies detected"],
                "cost": 0.001
            },
            "cost": 0.001
        }

    def generate_report(inputs):
        """Generate report from analysis."""
        analysis = inputs["analysis"]
        report = f"Analysis Report\n"
        report += f"Summary: {analysis['summary']}\n"
        report += f"Insights:\n"
        for insight in analysis["insights"]:
            report += f"  - {insight}\n"
        return {"report": report}

    engine = WorkflowEngine()
    engine.register_agent_implementation("validator", validate_data)
    engine.register_agent_implementation("analyzer", analyze_data)
    engine.register_agent_implementation("reporter", generate_report)

    print("Registered 3 agent implementations\n")

    # Example 5: Execute workflow
    print("5. Executing workflow")
    print("-" * 40)

    context = engine.execute_workflow(
        workflow=workflow,
        initial_inputs={
            "data": {
                "field1": "value1",
                "field2": "value2",
                "field3": "value3"
            }
        }
    )

    summary = context.get_summary()
    print(f"Execution completed:")
    print(f"  - Duration: {summary['duration_seconds']:.2f}s")
    print(f"  - Total executions: {summary['total_executions']}")
    print(f"  - Successful: {summary['successful_executions']}")
    print(f"  - Failed: {summary['failed_executions']}")
    print(f"  - Total cost: ${summary['total_cost']:.4f}")
    print(f"  - Has errors: {summary['has_errors']}\n")

    # Show final report
    if not context.has_errors():
        reporter_record = context.get_agent_record("reporter")
        if reporter_record and reporter_record.outputs:
            print("Final Report:")
            print("-" * 40)
            print(reporter_record.outputs["report"])

    print("\n=== Example Complete ===")


if __name__ == "__main__":
    main()
