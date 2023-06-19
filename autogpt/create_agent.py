from auto_gpt.agent import AgentPersist

# Create a new agent
agent = AgentPersist()

# Get the user's input
agent_name = input("What do you want to name the agent? ")

# Train the agent
agent.train(100)

# Save the agent to disk
agent.save(agent_name + ".pkl")
