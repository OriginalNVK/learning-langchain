# LangChain Course

Welcome to the LangChain Course repository! This repo contains all the code examples you'll need to follow along with the LangChain Master Class for Beginners. By the end of this course, you'll know how to use LangChain to create your own AI agents, build RAG chatbots, and automate tasks with AI.

## Course Outline

1. **Setup Environment**
2. **Chat Models**
3. **Prompt Templates**
4. **Chains**
5. **RAG (Retrieval-Augmented Generation)**
6. **Agents & Tools**

## Getting Started

### Prerequisites

- Python 3.10 or 3.11
- Poetry (Follow this [Poetry installation tutorial](https://python-poetry.org/docs/#installation) to install Poetry on your system)

### Installation

1. Clone the repository:

   ```bash
   <!-- TODO: UPDATE TO MY  -->
   git clone https://github.com/OriginalNVK/learning-langchain
   cd learning-langchain
   ```

2. Install dependencies using Poetry:

   ```bash
   poetry install --no-root
   ```

3. Set up your environment variables:

   - Rename the `.env.example` file to `.env` and update the variables inside with your own values. Example:

   ```bash
   mv .env.example .env
   ```

4. Activate the Poetry shell to run the examples:

   ```bash
   poetry shell
   ```

5. Run the code examples:

   ```bash
    python chat_models/basic.py
   ```

## Repository Structure

Here's a breakdown of the folders and what you'll find in each:

### 1. Chat Models

- `basic.py`
- `basic_conversation.py`
- `chat_alternatives.py`
- `conversation_with_user.py`
- `conversation_save_into_firestore.py`

Learn how to interact with models like ChatGPT, Claude, and Gemini.

### 2. Prompt Templates

- `basic.py`
- `template_with_chat_model.py`

Understand the basics of prompt templates and how to use them effectively.

### 3. Chains

- `basics.py`
- `chains_under_the_hood.py`
- `chains_extend.py`
- `chains_parallel.py`
- `chains_branches.py`

Learn how to create chains using Chat Models and Prompts to automate tasks.

### 4. RAG (Retrieval-Augmented Generation)

- `basic_v1.py`
- `basic_v2.py`
- `basic_metadata_v1.py`
- `basic_metadata_v2.py`
- `text_splitting_deep_dive.py`
- `embedding_deep_dive.py`
- `retriever_deep_dive.py`
- `rag_with_one_off_question.py`
- `rag_conversational.py`
- `crawl_scrape_advanced.py`
- `web_scrape_basic.py`

Explore the technologies like documents, embeddings, and vector stores that enable RAG queries.

### 5. Agents & Tools

- `agent_and_tool_basics.py`
- `agent_deep_dive/`
  - `agent_react_chat.py`
  - `agent_react_docstore.py`
- `tools_deep_dive/`
  - `constructor.py`
  - `base_tool.py`

Learn about agents, how they work, and how to build custom tools to enhance their capabilities.

## How to Use This Repository

1. **Watch the Video:** [langchain-master-class-for-beginner](https://www.youtube.com/watch?v=yF9kGESAi3M&t=11328s)

2. **Run the Code Examples:** Follow along with the code examples provided in this repository. Each section in the video corresponds to a folder in this repo.

3. **Supportive Materials:** If you get stuck or want to ask any question. Connect my facebook [here](https://www.facebook.com/vankhanh.47.2004).

## Comprehensive Documentation

Each script in this repository contains detailed comments explaining the purpose and functionality of the code. This will help you understand the flow and logic behind each example.

## FAQ

**Q: What is LangChain?**  
A: LangChain is a framework designed to simplify the process of building applications that utilize language models.

**Q: How do I set up my environment?**  
A: Follow the instructions in the "Getting Started" section above. Ensure you have Python 3.10 or 3.11 installed, install Poetry, clone the repository, install dependencies, rename the `.env.example` file to `.env`, and activate the Poetry shell.

**Q: I am getting an error when running the examples. What should I do?**  
A: Ensure all dependencies are installed correctly and your environment variables are set up properly. If the issue persists, seek help in the Skool community or open an issue on GitHub.

**Q: Can I contribute to this repository?**  
A: Yes! Contributions are welcome. Please open an issue or submit a pull request with your changes.

**Q: Where can I find more information about LangChain?**  
A: Check out the official LangChain documentation and join the Skool community for additional resources and support.

## Thank You 🙏

I would like to express my sincere gratitude to the YouTube channel for sharing the following video:  
[langchain-master-class-for-beginner](https://www.youtube.com/watch?v=yF9kGESAi3M&t=11328s)

This video has provided me with very valuable and practical knowledge.  
Thank you for taking the time and effort to teach and share such useful content with the community.

Your contribution is truly appreciated! 🌟
