# LangChain & LangGraph Learning Journey

Welcome to my comprehensive learning repository for LangChain and LangGraph! This repository contains practical examples, exercises, and implementations covering everything from basic chat models to advanced AI agents and graph-based workflows.

## 📁 Repository Structure

```
learning-langchain-langgraph/
├── learning-langchain/          # LangChain fundamentals and applications
└── learning-langgraph/          # LangGraph for building stateful AI agents
```

## 🚀 Learning Path Overview

This repository follows a structured learning approach from basic concepts to advanced implementations:

1. **Foundation**: Chat models, prompts, and basic chains
2. **Advanced Chains**: Parallel processing, branching, and extensions
3. **RAG Systems**: Document retrieval and question answering
4. **Agents & Tools**: Interactive AI agents with custom tools
5. **Graph-based AI**: Stateful workflows with LangGraph

---

## 📚 Learning-LangChain Section

### 1. Chat Models (`chat-models/`)

**What I Learned**: The foundation of LLM interactions in LangChain

#### Key Files:
- [`basic.py`](learning-langchain/chat-models/basic.py) - Basic ChatOpenAI model usage
- [`basic_conversation.py`](learning-langchain/chat-models/basic_conversation.py) - Simple conversational flows
- [`conversation_save_into_firebase.py`](learning-langchain/chat-models/conversation_save_into_firebase.py) - Persistent chat history with Firestore

#### Core Concepts:
- **Model Initialization**: Using [`ChatOpenAI`](learning-langchain/chat-models/conversation_save_into_firebase.py) with different models (gpt-4o)
- **Message Types**: [`HumanMessage`](learning-langchain/chat-models/conversation_save_into_firebase.py), [`AIMessage`](learning-langchain/chat-models/conversation_save_into_firebase.py), [`SystemMessage`](learning-langchain/chat-models/conversation_save_into_firebase.py)
- **Persistent History**: Using [`FirestoreChatMessageHistory`](learning-langchain/chat-models/conversation_save_into_firebase.py) for conversation storage

### 2. Prompt Templates (`prompt_template/`)

**What I Learned**: Structured prompt creation and management

#### Core Concepts:
- **Template Structure**: Using [`ChatPromptTemplate.from_messages`](learning-langchain/chains/basic.py)
- **Variable Substitution**: Dynamic content insertion with placeholders
- **Message Composition**: Combining system and human messages effectively

### 3. Chains (`chains/`)

**What I Learned**: Building complex workflows by chaining components

#### Key Files:
- [`basic.py`](learning-langchain/chains/basic.py) - Simple chain creation with prompts and models
- [`chains_parallel.py`](learning-langchain/chains/chains_parallel.py) - Parallel execution using [`RunnableParallel`](learning-langchain/chains/chains_parallel.py)
- [`chains_branches.py`](learning-langchain/chains/chains_branches.py) - Conditional logic with [`RunnableBranch`](learning-langchain/chains/chains_branches.py)
- [`chains_extend.py`](learning-langchain/chains/chains_extend.py) - Chain extensions with [`RunnableLambda`](learning-langchain/chains/chains_extend.py)
- [`chains_under_the_hood.py`](learning-langchain/chains/chains_under_the_hood.py) - Manual chain construction with [`RunnableSequence`](learning-langchain/chains/chains_under_the_hood.py)

#### Core Concepts:
- **Basic Chaining**: `prompt_template | model | StrOutputParser()`
- **Parallel Processing**: Executing multiple branches simultaneously
- **Conditional Logic**: Routing based on input characteristics
- **Custom Functions**: Integrating custom logic with [`RunnableLambda`](learning-langchain/chains/chains_extend.py)

### 4. RAG (Retrieval-Augmented Generation) (`rag/`)

**What I Learned**: Building systems that combine document retrieval with language models

#### Key Files:
- [`basic_v1.py`](learning-langchain/rag/basic_v1.py) & [`basic_v2.py`](learning-langchain/rag/basic_v2.py) - Foundation RAG implementations
- [`basic_metadata_v1.py`](learning-langchain/rag/basic_metadata_v1.py) & [`basic_metadata_v2.py`](learning-langchain/rag/basic_metadata_v2.py) - Document metadata handling
- [`text_splitting_deep_dive.py`](learning-langchain/rag/text_splitting_deep_dive.py) - Advanced text chunking strategies
- [`embedding_deep_dive.py`](learning-langchain/rag/embedding_deep_dive.py) - Comparing different embedding models
- [`rag_conversation.py`](learning-langchain/rag/rag_conversation.py) - Conversational RAG systems
- [`web_scrape_basic.py`](learning-langchain/rag/web_scrape_basic.py) - Web content ingestion

#### Core Concepts:
- **Document Loading**: Using [`TextLoader`](learning-langchain/rag/basic_v1.py) for various file formats
- **Text Splitting**: 
  - [`CharacterTextSplitter`](learning-langchain/rag/text_splitting_deep_dive.py) - Simple character-based splitting
  - [`RecursiveCharacterTextSplitter`](learning-langchain/rag/text_splitting_deep_dive.py) - Context-preserving splitting
  - [`TokenTextSplitter`](learning-langchain/rag/text_splitting_deep_dive.py) - Token-based chunking
  - [`SentenceTransformersTokenTextSplitter`](learning-langchain/rag/text_splitting_deep_dive.py) - Semantic splitting
- **Embeddings**: Using [`OpenAIEmbeddings`](learning-langchain/rag/basic_v1.py) with text-embedding-3-small model
- **Vector Storage**: [`Chroma`](learning-langchain/rag/basic_v1.py) for persistent vector databases
- **Retrieval**: Similarity search with score thresholds
- **Metadata Management**: Tracking document sources and contexts

#### Sample Books Used:
- [`odyssey.txt`](learning-langchain/rag/books/odyssey.txt) - Classic literature for testing
- [`romeo_and_juliet.txt`](learning-langchain/rag/books/romeo_and_juliet.txt) - Shakespeare content
- [`us_bill_of_rights.txt`](learning-langchain/rag/books/us_bill_of_rights.txt) - Legal documents
- [`langchain_demo.txt`](learning-langchain/rag/books/langchain_demo.txt) - Technical documentation

### 5. Agents & Tools (`agents_&_tools/`)

**What I Learned**: Creating intelligent agents that can use tools and make decisions

#### Key Files:
- [`agent_and_tool_basic.py`](learning-langchain/agents_&_tools/agent_and_tool_basic.py) - Basic agent concepts
- [`agents_deep_dive/agent_react_docstore.py`](learning-langchain/agents_&_tools/agents_deep_dive/agent_react_docstore.py) - ReAct pattern with document retrieval

#### Core Concepts:
- **ReAct Pattern**: Reasoning and Acting with [`create_react_agent`](learning-langchain/agents_&_tools/agents_deep_dive/agent_react_docstore.py)
- **Tool Integration**: Custom tools with [`Tool`](learning-langchain/agents_&_tools/agents_deep_dive/agent_react_docstore.py) class
- **Agent Execution**: Using [`AgentExecutor`](learning-langchain/agents_&_tools/agents_deep_dive/agent_react_docstore.py)
- **RAG Integration**: Combining retrieval with agent decision-making

---

## 🔗 Learning-LangGraph Section

### 1. Basic Agent Implementation (`agent-basic/`)

**What I Learned**: Transitioning from chains to stateful graph-based agents

#### Core Concepts:
- **State Management**: Maintaining conversation context across interactions
- **Graph Architecture**: Node-based workflow design
- **Conditional Routing**: Dynamic path selection based on state

### 2. AI Agent Development (`AI-Agent/`)

**What I Learned**: Building sophisticated agents with specialized capabilities

#### Key Files:
- [`drafter.py`](learning-langgraph/AI-Agent/drafter.py) - Document drafting agent with tools
- [`RAG_Agent.py`](learning-langgraph/AI-Agent/RAG_Agent.py) - RAG-powered agent with PDF processing

#### Core Concepts from Drafter Agent:
- **State Definition**: Using [`TypedDict`](learning-langgraph/AI-Agent/drafter.py) for structured state
- **Tool Implementation**: Custom tools with [`@tool`](learning-langgraph/AI-Agent/drafter.py) decorator
  - [`update`](learning-langgraph/AI-Agent/drafter.py) - Document content modification
  - [`save`](learning-langgraph/AI-Agent/drafter.py) - File persistence
- **Graph Construction**: [`StateGraph`](learning-langgraph/AI-Agent/drafter.py) with nodes and edges
- **Tool Binding**: Connecting tools to language models
- **Conditional Logic**: [`should_continue`](learning-langgraph/AI-Agent/drafter.py) for flow control

#### Core Concepts from RAG Agent:
- **PDF Processing**: Using [`PyPDFLoader`](learning-langgraph/AI-Agent/RAG_Agent.py) for document ingestion
- **Vector Database**: [`Chroma`](learning-langgraph/AI-Agent/RAG_Agent.py) for semantic search
- **Embedding Integration**: [`OpenAIEmbeddings`](learning-langgraph/AI-Agent/RAG_Agent.py) for document vectorization
- **Retrieval Tools**: Custom retrieval functions as agent tools
- **Error Handling**: Robust file existence and loading validation

### 3. Basic Exercises (`exercises_basic/`)

**What I Learned**: Practical applications and hands-on implementation

#### Core Concepts:
- **Graph Visualization**: Understanding workflow structures
- **State Transitions**: Managing complex agent behaviors
- **Tool Orchestration**: Coordinating multiple capabilities

---

## 🛠️ Technical Stack

### Core Libraries:
- **LangChain**: Framework for LLM applications
- **LangGraph**: State-based agent workflows
- **OpenAI**: Language models and embeddings
- **Chroma**: Vector database for similarity search
- **Firestore**: Persistent conversation storage

### Development Tools:
- **Poetry**: Dependency management
- **Python 3.10+**: Runtime environment
- **dotenv**: Environment variable management

---

## 🎯 Key Learning Outcomes

### 1. **Chain Architecture Mastery**
- Built linear, parallel, and conditional processing pipelines
- Implemented custom logic with RunnableLambda
- Mastered prompt template integration

### 2. **RAG System Expertise**
- Designed document ingestion and chunking strategies
- Implemented semantic search with vector databases
- Created conversational RAG systems with memory

### 3. **Agent Development Skills**
- Built ReAct pattern agents with tool usage
- Implemented stateful workflows with LangGraph
- Created specialized agents for document processing

### 4. **Production Considerations**
- Persistent storage solutions (Chroma, Firestore)
- Error handling and validation
- Metadata management for traceability

---

## 🚀 Next Steps

Based on this learning journey, potential areas for expansion include:

1. **Multi-Agent Systems**: Coordinating multiple specialized agents
2. **Advanced Tool Integration**: API calls, database queries, external services
3. **Production Deployment**: Scaling and monitoring considerations
4. **Custom Model Fine-tuning**: Domain-specific adaptations
5. **Advanced Graph Patterns**: Complex workflow orchestration

---

## 📖 Resources

- **LangChain Documentation**: [python.langchain.com](https://python.langchain.com/)
- **LangGraph Documentation**: Official LangGraph guides
- **Course Reference**: [LangChain Master Class for Beginners](https://www.youtube.com/watch?v=yF9kGESAi3M&t=11328s)

---

*This repository represents a comprehensive journey through modern AI application development, from basic chat interactions to sophisticated agent-based systems. Each example builds upon previous concepts, creating a solid foundation for real-world AI application development.*