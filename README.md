# GitHub Models Actions Examples 🚀🤖

[![AI Code Complexity Analyzer](https://github.com/your-org/your-repo/actions/workflows/ai-code-review.yml/badge.svg)](../../actions/workflows/ai-code-review.yml)
[![AI PR Description Generator](https://github.com/your-org/your-repo/actions/workflows/ai-pr-description.yml/badge.svg)](../../actions/workflows/ai-pr-description.yml)

<!--
These badges show the status of the last workflow run (success or failure) for each workflow.
-->

This repository demonstrates how to use AI models (With instructiuon for using GitHub Models as the inference provider) within GitHub Actions workflows. The examples show how to automate code review and pull request description generation using AI.

---

## ✨ Workflows Included

- **AI Code Complexity Analyzer** (`ai-code-review.yml`):
  - 🧠 Analyzes JavaScript files for code complexity using an AI model.
  - 💬 Posts a summary of the analysis as a commit comment.

- **AI PR Description Generator** (`ai-pr-description.yml`):
  - 📝 Generates informative pull request descriptions based on code diffs using an AI model.

---

## ⚡️ Quick Setup

1. **🔐 Add GitHub Secrets**
   - Go to your repository Settings → Secrets and variables → Actions.
   - Add the following secrets:
     - `OPENAI_API_KEY`: Your OpenAI API key.
     - `OPENAI_API_ENDPOINT`: The OpenAI-compatible API endpoint (e.g., `https://models.github.ai/inference`).
     - `OPENAI_MODEL`: The model name to use (e.g., `gpt-3.5-turbo`).

2. **📄 (Optional) Environment Variables**
   - See `.env.example` for reference, but do not commit real secrets.

---

## 🔑 How to Get Your GitHub Personal Access Token (PAT) for GitHub Models

To use GitHub Models APIs in this repository, you need a GitHub Personal Access Token (PAT) with the appropriate scopes. Here’s how:

1. **Get Your Personal Access Token (PAT):**
   - Go to [GitHub Personal Access Tokens](https://github.com/settings/tokens).
   - Click **Generate new token** (classic or fine-grained).
   - Select the necessary scopes for Models API access (typically `read:org`, `user`, and `codespace` if needed).
   - Copy the generated token and use it as your `OPENAI_API_KEY`.

2. **Get the API Endpoint:**
   - For GitHub Models, use the endpoint: `https://models.github.ai/inference` as your `OPENAI_API_ENDPOINT`.

3. **Get the Model Name:**
   - For GitHub Models, you can use model names like `openai/gpt-4.1` or `deepseek/DeepSeek-V3-0324`.
   - Set this as your `OPENAI_MODEL` secret.

4. **Add Secrets to Your Fork:**
   - In your forked repository, go to **Settings → Secrets and variables → Actions**.
   - Click **New repository secret** for each of the following:
     - `OPENAI_API_KEY`: Paste your PAT here.
     - `OPENAI_API_ENDPOINT`: Use `https://models.github.ai/inference`.
     - `OPENAI_MODEL`: Use your chosen model name (e.g., `openai/gpt-4.1`).

Once these secrets are set, the workflows in this repo will use your GitHub Models API access!

---

## 🎯 Purpose

This repo is for demonstration and educational purposes, showing how to integrate large language models into GitHub Actions workflows for automation and code intelligence.

---

> 💡 **Feel free to fork and adapt for your own use cases!**

---

Made with ❤️ by the @robertefreeman for @briancl2 .
