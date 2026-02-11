# Applied AI Engineering for the Enterprise
## Day 3 - AI Agents
## Session labs 
## Revision 1.8 - 02/10/26

**Follow the startup instructions in the README.md file IF NOT ALREADY DONE!**

**NOTE: To copy and paste in the codespace, you may need to use keyboard commands - CTRL-C and CTRL-V. Chrome may work best for this.**

<br><br>

**Lab 1 - Creating a simple agent**

**Purpose: In this lab, we’ll learn about the basics of agents and see how tools are called. We'll also see how Chain of Thought prompting works with LLMs and how we can have ReAct agents reason and act.**

---

**What the agent example does**
- Uses a local Ollama-served LLM (llama3.2) to interpret natural language queries about weather.
- Extracts coordinates from the input, queries Open-Meteo for weather data.
- Converts temperatures and provides a summary forecast using a TAO loop.

**What it demonstrates about the framework**
- Shows how to integrate **LangChain + Ollama** to drive LLM reasoning.
- Demonstrates **Chain of Thought** reasoning with `Thought → Action → Observation` steps.
- Introduces simple function/tool calling with a deterministic LLM interface.

--- 

### Steps

1. In our repository, we have a set of Python programs that we'll be building out to work with concepts in the labs. These are mostly in the *agents* subdirectory. Go to the *TERMINAL* tab in the bottom part of your IDE and change into that directory.
```
cd agents
```

<br><br>


2. For this lab, we have the outline of an agent in a file called *agent1.py* in that directory. You can take a look at the code either by clicking on [**agents/agent1.py**](./agents/agent1.py) or by entering the command below in the codespace's terminal.
   
```
code agent1.py
```

<br><br>

3. If you scroll through this file, you can see it outlines the steps the agent will go through without all the code. When you are done looking at it, close the file by clicking on the "X" in the tab at the top of the file.

<br><br>

4. Now, let's fill in the code. To keep things simple and avoid formatting/typing frustration, we already have the code in another file that we can merge into this one. Run the command below in the terminal.
```
code -d ../extra/lab1-code.txt agent1.py
```

<br><br>

5. Once you have run the command, you'll have a side-by-side view in your editor of the completed code and the *agent1.py* file.
  You can merge each section of code into the *agent1.py* file by hovering over the middle bar and clicking on the arrows pointing right. Go through each section, look at the code, and then click to merge the changes in, one at a time.

![Side-by-side merge](./images/aa40.png?raw=true "Side-by-side merge") 

<br><br>

6. When you have finished merging all the sections in, the files should show no differences. Save the changes simply by clicking on the "X" in the tab name.

![Merge complete](./images/aa41.png?raw=true "Merge complete") 

<br><br>

7. Now you can run your agent with the following command:

```
python agent1.py
```

<br><br>

8. The agent will start running and will prompt for a location (or "exit" to finish). (This may take a while to run.) At the prompt, you can type in a location like "Paris, France" or "London" or "Raleigh" and hit *Enter*. After that you'll be able to see the Thought -> Action -> Observation loop in practice as each one is listed out. You'll also see the arguments being passed to the tools as they are called. Finally you should see a human-friendly message from the AI summarizing the weather forecast.

![Agent run](./images/ae36.png?raw=true "Agent run") 

<br><br>

9. You can then input another location and run the agent again or exit. Note that the API may be limiting the number of accesses in a short period of time and so you may see the agent retrying.

10. Try putting in *Sydney, Australia* and then check the output against the weather forecast on the web. Why do you think it doesn't match? How would you fix it?

Here's a clue: "If latitude/longitude is in the Southern or Western hemisphere, use negative values as appropriate"

<p align="center">
<b>[END OF LAB]</b>
</p>
</br></br>

**Lab 2 - Leveraging Coding Agents and Persistence**

**Purpose: In this lab, we’ll see how agents can drive solutions via creating code and implementing simple memory techniques - using the smolagents framework.**

---

**What the agent example does**
- Uses SmolAgents to convert currencies and remember past conversions.
- Accepts incomplete input (e.g., “convert 200”) and fills in missing parts from memory.
- Stores memory in a local JSON file to persist state across sessions.

**What it demonstrates about the framework**
- Introduces the **SmolAgents CodeAgent**, a declarative and lightweight ReAct agent.
- Demonstrates **@tool decorators**, deterministic execution, and **tool chaining**.
- Highlights pluggable **memory support**, custom tools, and precise control over the agent loop.

---

### Steps

1. For this lab, we have a simple application that does currency conversion using prompts of the form "Convert 100 USD to EUR", where *USD* = US dollars and *EUR* = euros.  It will also remember previous values and invocations.

<br><br>

2. As before, we'll use the "view differences and merge" technique to learn about the code we'll be working with. The command to run this time is below:

```
code -d ../extra/curr_conv_agent.txt curr_conv_agent.py
```
<br>

The code in this application showcases several SmolAgents features and agent techniques including the following. See how many you can identify as your reviewing the code.

- **@tool decorator** turns your Python functions into callable “tools” for the agent.  
- **LiteLLMModel** plugs in your local Ollama llama3.2 as the agent’s reasoning engine.  
- **CodeAgent** runs a ReAct loop: think (LLM), act (call tool), observe, repeat.  
- **Memory feature** remembers current values and persists them (with history) to an external JSON file.

<br>

![Code for memory agent](./images/aia-2-9.png?raw=true "Code for memory agent") 

<br><br>

3. When you're done merging, close the tab as usual to save your changes. Now, in a terminal, run the agent with the command below:

```
python curr_conv_agent.py
```

<br><br>

4. Enter a basic prompt like the one below.

```
Convert 100 USD to EUR
```

![Running agent](./images/ae37.png?raw=true "Running agent") 

<br><br>

5. The agent may pause for a bit as the LLM loads and the processing happens. When it is finished with this run, you'll see output like the screenshot below. Notice that since we used the SmolAgents CodeAgent type, you can see the code it created and executed in the black box. While you are waiting on it to complete, this is a good time to go back and look at the code in *curr_conv_agent.py* to understand more about it.

![Running agent](./images/ae38.png?raw=true "Running agent")   

<br><br>

6. Now you can try some partial inputs with missing values to demonstrate the agent remembering arguments that were passed to it before. Here are some to try. Output is shown in the screenshot. (You may see some intermediate steps. You're looking for the one with "Final answer" in it.)

```
Convert 200
Convert 400 to JPY
```

![Running with partial inputs](./images/aa70.png?raw=true "Running agent")  
![Running with partial inputs](./images/aa71.png?raw=true "Running agent")   


7. To see the stored history information on disk, type "exit" to exit the tool. Then in the terminal type the command below to see the contents of the file.

```
cat currency_memory.json
```

![Looking at memory file](./images/ae41.png?raw=true "Looking at memory file") 

8. Finally, you can start the agent again and enter "history" at the prompt to see the persisted history from before. Then you can try a query and it should pick up as before. In the example, we used the query below:

```
python curr_conv_agent.py
convert 300
```

![Running with partial inputs](./images/ae42.png?raw=true "Running agent")   


9.  Just type "exit" when ready to quit the tool.

<p align="center">
<b>[END OF LAB]</b>
</p>
</br></br>

    
**Lab 3 - Using RAG with Agents - Enhanced with Memory and Context Awareness**

**Purpose: In this lab, we'll build an intelligent RAG agent that maintains conversation memory and handles follow-up questions**

---

**What the agent example does**
- Uses a proper three-step RAG pattern: **Retrieve → Augment → Generate**
- **Maintains conversation memory** across queries
- **Detects and handles follow-up questions** intelligently
- **Caches query results** for improved performance
- Augments prompts with both retrieved context and conversation history
- Provides source citations for transparency

**What makes this an AGENT (not just a RAG system)**
- **Conversation Memory**: Remembers last 3 exchanges for contextual understanding
- **Follow-up Detection**: Recognizes when you're asking about "that" or "it"
- **Smart Caching**: Reuses recent search results when appropriate
- **Contextual Responses**: Says "As we discussed earlier..." when referencing past answers
- **Stateful Interaction**: Unlike simple Q&A, maintains state across queries

---

### Steps

1. For this lab, we'll be using a comprehensive knowledge base of OmniTech company documentation including returns policies, device troubleshooting, shipping logistics, and account security. These PDFs are located in [**knowledge_base_pdfs/**](./knowledge_base_pdfs/)

<br><br>

2. We'll also be using a smaller model to fit better in our environment. You can verify that the *llama3.2:1b* model is present using the first command below. If it is not for some reason, you can use the second command get it.

```
ollama list
ollama pull llama3.2:1b
```

![Getting new model](./images/ae43.png?raw=true "Getting new model")

<br><br>

3. Now, we need to create the vector database from our PDFs. This will chunk the documents, create embeddings, and store them in ChromaDB. Change to the agents directory if you're not already there, and run the indexing tool to create the vector database. This uses the same best practices from Day 2 including semantic chunking, table extraction, and rich metadata:

```
cd agents
python ../tools/index_pdfs.py --pdf-dir ../knowledge_base_pdfs --chroma-path ./chroma_db
```

You should see output showing the PDFs being processed and chunks being indexed.

![Indexing PDFs](./images/ae44.png?raw=true "Indexing PDFs")

<br><br>

4. As before, we'll use the "view differences and merge" technique to build our RAG agent. The updated code incorporates all the best practices including the three-step RAG pattern:

```
code -d ../extra/rag_agent.txt rag_agent.py
```

Notice the three key methods in the code:
- `RETRIEVE` - Searches the vector database for relevant chunks
- `AUGMENT` - Augments the user query with retrieved context
- `GENERATE` - Calls the LLM to generate a grounded answer

![Code for rag agent](./images/aia-2-15.png?raw=true "Code for rag agent")

<br><br>

5. When you're done merging, close the tab as usual to save your changes. Now, in a terminal, run the agent:

```
python rag_agent.py
```

<br><br>

6. You'll see the agent connect to the ChromaDB database and display statistics about the knowledge base including total chunks and source documents. It will also check that Ollama is running with the correct model.

![RAG initialization](./images/ae45.png?raw=true "RAG initialization")

<br><br>

7. The system will show example questions with follow-up suggestions. Notice the agent features like memory status and special commands. Try this conversation sequence:

**First question:**
```
How can I return a product?
```
The agent will provide a detailed answer with sources.

![First question](./images/ae46.png?raw=true "First question")

<br><br>

8. Now let's try a follow-up question to demonstrate the use of the agent's memory. Try this question.

```
Tell me more about the timeframe
```
Notice: The agent detects this as a follow-up and includes conversation context!

<br><br>

You'll see the agent's *intelligence* in action:
   - **[AGENT MEMORY]** messages when it detects follow-ups
   - **[RETRIEVE]** with caching (may say "Using cached results")
   - **Memory status** showing conversation length and cached queries
   - Contextual answers like "As we discussed earlier..."

![Agent memory in action](./images/ae47.png?raw=true "Agent memory in action")

<br><br>

9. Try another conversation thread to see memory handling:

```
What are the shipping costs?
```
Then follow with:
```
What about national?
```

The agent understands "national" refers to shipping without you saying "national shipping costs"!

![Agent memory in action](./images/ae48.png?raw=true "Agent memory in action")

<br><br>

10. You can also see the response when you ask a question that the agent doesn't have any information about.
   - Ask about something NOT in docs: `What's the CEO's favorite color?`
   
![Follow-up](./images/ae49.png?raw=true "Follow-up")

<br><br>

11. Try clearing the context and then asking one of the questions again. You should see that the agent doesn't continue the previous conversation.

```
clear
What about national?
```

![Cleared context](./images/ae162.png?raw=true "Cleared context")

<br><br>

12. After exploring, type `exit` to quit. The agent will show how many queries it processed since the context was started/cleared.

**Key Takeaways - What Makes This an Agent:**
- **Memory & State**: Unlike simple RAG, this agent maintains conversation history
- **Context Awareness**: Detects and handles follow-up questions intelligently
- **Performance Optimization**: Caches queries to avoid redundant searches
- **Natural Conversation**: Understands pronouns and contextual references
- **Agent Behavior**: This is how agents differ from stateless Q&A systems - they remember, learn, and adapt within a session

<p align="center">
<b>[END OF LAB]</b>
</p>
</br></br>


**Lab 4 - Building Multiagent workflows with the Reflective Pattern**

**Purpose: In this lab, we’ll see how to create a multiagent workflow that uses the reflective pattern using the AutoGen framework.** 

**NOTE: This process generates and runs code via a subprocess, but with the full permissions of the user. It is for educational purposes only and is not secure.**

---

**What the multiagent example does**
- Accepts a user request to generate Python code (e.g., “Plot a sine wave”).
- Uses a **code writer agent** to generate the initial response.
- Simulates execution of the generated code in a **sandboxed subprocess**, capturing any runtime output or errors.
- Passes the code (with runtime feedback) to a **critic agent** that assesses whether the code meets the original request.
- If the critic returns a `FAIL`, the code is passed to a **fixer agent** to revise it.
- Simulates execution of the **fixed code** as well and reports runtime behavior.
- Outputs either the original or revised code with a self-improvement cycle.

**What it demonstrates about the framework**
- Demonstrates **AutoGen’s modular agent design**, with roles like code writer, critic, and fixer.
- Uses **structured messaging** and system prompts to guide agent roles and ensure predictable output.
- Shows how to build **reflection patterns** with execution-aware feedback:  
  **generate → simulate → evaluate → revise → simulate**.
- Enhances LLM reliability by integrating **actual runtime behavior** into the critique loop.

---

### Steps


1. As we've done before, we'll build out the agent code with the diff/merge facility. Run the command below.
```
code -d ../extra/reflect_agent.txt reflect_agent.py
```

![Diffs](./images/aip11.png?raw=true "Diffs") 

<br>

**This time you'll be merging in the following sections:**

- agent to write code
- agent to review code
- agent to fix code
- section to exec the code (note this only works if no additional imports are required)
- workflow sections to drive the agents

<br><br>

2. When you're done merging, close the tab as usual to save your changes. Now, in a terminal, run the agent with the command below:

```
python reflect_agent.py
```

<br><br>

3. After the agent starts, you'll be at a prompt that says "Request >". This is waiting for you to input a programming request. Let's start with something simple like the prompt below. Just type this in and hit Enter.

```
determine if a number is prime or not
```

![Simple task](./images/ae50.png?raw=true "Simple task")

<br><br>

4. After this, you should see a "Generating Code..." message indicating the coding agent is generating code. Then you'll see the suggested code.

![Suggested code](./images/ae51.png?raw=true "Suggested code")

<br><br>

5. Next, you'll see where the agent tried to run the code and provides "Runtime Feedback" indicating whether or not it executed successfully. That's followed by the "Critique" and the PASS/FAIL verdict.

![Code evaluation](./images/aia-2-22.png?raw=true "Code evaluation")

<br><br>
 
6. This one probably passed on the first round. The agent will be ready for another task. Let's see what it's like when there's an error. Try the following prompt:

```
Determine if a number is prime or not, but inject an error. Do not include a comment about the error.
```

<br><br>

7. After this runs, and the initial code is generated, you should see the "Critique" section noting this as a "FAIL". The agent will then attempt to automatically fix the code and suggest "Fixed Code". Then it will attempt to execute the fixed code it generated. If all goes well, you'll see a message after that indicating that the fixed code was "Executed successfully."

![Fix run](./images/ae52.png?raw=true "Fix run")

<br><br>

8. Let's try one more change. Use "*exit*" to stop the current agent. We have a version of the code that has some extra functionality built-in to stream output, print system_messages, show when an agent is running, etc. It's in the "extra" directory, under "reflect_agent_verbose.py". Go ahead and run that and try a prompt with it. You can try the same prompt as in step 6 if you want. (You can type "exit" to stop the running one.)

```
python ../extra/reflect_agent_verbose.py
```

![Verbose run](./images/aip10.png?raw=true "Verbose run")

<br><br>

9. (Optional) After this you can try other queries with the original file or the verbose one if you want. Or you can try changing some of the system messages in the code and re-running it if you like to try a larger change.

<br><br>

<p align="center">
<b>[END OF LAB]</b>
</p>
</br></br>


**Lab 5 - Testing Agent Reasoning and Tool Selection**

**Purpose: Learn to validate agent behavior - testing if agents reason correctly, select appropriate tools, and handle edge cases.**

---

**What you'll test:**
- Agent tool selection logic
- Reasoning with ambiguous queries
- Error recovery behavior
- One real agent reasoning test (llama3.2)

**What it demonstrates:**
- How to verify agent decision-making
- Testing reasoning patterns (ReAct loop)
- Mocking for fast iteration, then real validation
- Catching faulty agent logic before production

---

### Steps

1. We have an agent with multiple tools (calculator, weather, currency). The agent must REASON about which tool to use. View the test file:
```
code test_agent_reasoning.py
```

<br><br>

2. Scroll down to the sections that start with "# ==== MOCK-BASED TESTS" (around line 143). Notice the test structures throughout the rest of the file:
   - Mock LLM returns (instant - no waiting)
   - Tests verify: "Did agent choose calculator for math?"
   - Tests verify: "Did agent choose weather for location query?"
   - Agent reasoning logic tested, not LLM quality

![Testing structure](./images/ae53.png?raw=true "Testing structure")

<br><br>

3. Run the mock-based reasoning tests (instant). Note: Use `python -m pytest` and add `-s` flag to see test output:
```
python -m pytest test_agent_reasoning.py::test_agent_selects_calculator -v -s
python -m pytest test_agent_reasoning.py::test_agent_selects_weather -v -s
```

You should see output showing what each test validates. The `-s` flag shows print statements so you can see what's being tested.

![Passing test](./images/ae163.png?raw=true "Passing test")

<br><br>

4. These pass instantly because we're testing the agent's tool routing logic with predetermined responses. Now let's test ambiguity handling:
```
python -m pytest test_agent_reasoning.py::test_ambiguous_query -v -s
```

<br><br>

5. This test verifies the agent asks for clarification when query is unclear. All instant because LLM responses are mocked.

![Passing test](./images/ae55.png?raw=true "Passing test")

<br><br>

6. Now let's test error recovery - what happens when a tool fails?
```
python -m pytest test_agent_reasoning.py::test_tool_failure_recovery -v -s
```
<br><br>

7. Watch the output - you'll see the tool return an error message (not crash), demonstrating that the agent can receive errors and explain them to users. This completes instantly with mocked responses.

![Passing test](./images/ae56.png?raw=true "Passing test")

<br><br>

8. Now the real test: Let's verify actual agent reasoning with the model. This tests if the agent can REASON about which tool to use:
```
python -m pytest test_agent_reasoning.py::test_real_agent_tool_selection -v -s
```

This will do the following: 
- Give agent: "What's 25 times 4 and what's the weather in Tokyo?"
- Test that agent correctly identifies TWO tasks
- Test that agent calls BOTH tools (calculator AND weather)
- Verify agent reasoning chain

![Passing test](./images/ae57.png?raw=true "Passing test")

<br><br>


9. While waiting, open the test to see what's being validated:
```
code test_agent_reasoning.py
```

Look at `test_real_agent_tool_selection()` (around line 310) - it checks:
- Did agent parse the compound query?
- Did agent sequence tool calls correctly?
- Did agent synthesize results?

10. After completion, review the key insight: We tested agent behavior (reasoning, tool selection, error handling) not just code correctness. This is agentic testing.

<br><br>

### Production Testing Considerations

**Note**: This lab covers unit and basic integration testing with mocked LLM responses for fast iteration, plus one real validation test. For production agent systems, you should also implement:

**Additional Test Types**:
- **End-to-end workflow tests**: Test complete user journeys through multi-step agent workflows
- **Performance/load testing**: Validate response times under various loads and concurrent users
- **Regression testing**: Ensure agent behavior remains consistent across LLM model updates
- **Edge case testing**: Test unusual inputs, ambiguous queries, and boundary conditions

**Monitoring & Observability**:
- Implement logging for all agent decisions and tool calls
- Use LLM observability platforms (LangSmith, Weights & Biases, Arize)
- Track metrics: success rate, average response time, tool call accuracy, user satisfaction
- Set up alerts for anomalous behavior or degraded performance

**Testing Best Practices**:
- Mock LLM calls for 90% of tests (speed + determinism)
- Use small, fast models (like llama3.2:1b) for integration tests
- Reserve full model testing for critical user paths only
- Version control your test prompts and expected behaviors
- Maintain a test suite that covers your agent's "safety rails"

<p align="center">
**[END OF LAB]**
</p>
</br></br>



<p align="center">
<b>[END OF LAB]</b>
</p>
</br></br>


<p align="center">
**THANKS!**
</p>


