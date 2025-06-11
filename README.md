# GitHub Models Actions Examples 🚀🤖

[![AI Code Complexity Analyzer](https://github.com/robertefreeman/GH-Models-actions-examples/actions/workflows/ai-code-review.yml/badge.svg)](https://github.com/robertefreeman/GH-Models-actions-examples/actions/workflows/ai-code-review.yml)
[![AI PR Description Generator](https://github.com/robertefreeman/GH-Models-actions-examples/actions/workflows/ai-pr-description.yml/badge.svg)](https://github.com/robertefreeman/GH-Models-actions-examples/actions/workflows/ai-pr-description.yml)
[![AI Project Summary Generator](https://github.com/robertefreeman/GH-Models-actions-examples/actions/workflows/ai-project-summary.yml/badge.svg)](https://github.com/robertefreeman/GH-Models-actions-examples/actions/workflows/ai-project-summary.yml)

<!--
These badges show the status of the last workflow run (success or failure) for each workflow.
-->

This repository demonstrates how to use **GitHub Models** within GitHub Actions workflows for intelligent code automation. The examples show practical implementations of GitHub's hosted AI models for code analysis, pull request enhancement, and project documentation generation - all running natively within your GitHub Actions pipelines!

---

## ✨ Workflows Included

- **AI Code Complexity Analyzer** (`ai-code-review.yml`):
  - 🧠 Analyzes JavaScript files for code complexity using GitHub Models.
  - 💬 Posts detailed analysis reports with complexity insights and recommendations.

- **AI PR Description Generator** (`ai-pr-description.yml`):
  - 📝 Generates informative pull request descriptions from code diffs using GitHub Models.
  - 🎯 Automatically enhances PRs with AI-powered summaries and impact analysis.

- **AI Project Summary Generator** (`ai-project-summary.yml`):
  - 📊 Creates comprehensive project documentation (`projectsummary.md`) using GitHub Models.
  - 🤖 Analyzes codebase structure and generates intelligent documentation for AI coding agents.

---

## ⚡️ Quick Setup

1. **🔐 Add GitHub Secrets**
   - Go to your repository Settings → Secrets and variables → Actions.
   - Add the following secrets for GitHub Models API access:
     - `OPENAI_API_KEY`: Your GitHub Personal Access Token (PAT).
     - `OPENAI_API_ENDPOINT`: The GitHub Models API endpoint (e.g., `https://models.inference.ai.azure.com`).
     - `OPENAI_MODEL`: The GitHub Models model name (e.g., `gpt-4o`, `gpt-3.5-turbo`).

2. **🎮 Running the Workflows**
   - **AI Code Complexity Analyzer**: Runs automatically on pushes to JavaScript files
   - **AI PR Description Generator**: Runs automatically when pull requests are opened/updated
   - **AI Project Summary Generator**: Runs on pushes to main branch or manually via GitHub Actions tab → "Run workflow"

3. **📄 (Optional) Environment Variables**
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
   - For GitHub Models, use the endpoint: `https://models.inference.ai.azure.com` as your `OPENAI_API_ENDPOINT`.
   - Alternative GitHub Models endpoints may include `https://models.ai.azure.com` or check your GitHub Models dashboard for the correct URL.

3. **Choose Your GitHub Models Model:**
   - GitHub Models supports various AI models: `gpt-4o`, `gpt-3.5-turbo`, `claude-3-sonnet`, etc.
   - Set your chosen model name as the `OPENAI_MODEL` secret.

4. **Add Secrets to Your Repository:**
   - In your repository, go to **Settings → Secrets and variables → Actions**.
   - Add these repository secrets:
     - `OPENAI_API_KEY`: Your GitHub PAT
     - `OPENAI_API_ENDPOINT`: `https://models.inference.ai.azure.com`
     - `OPENAI_MODEL`: Your chosen model (e.g., `gpt-4o`)

Once configured, your GitHub Actions workflows will use GitHub Models for intelligent automation!

---

## 🎯 Purpose

This repository showcases practical examples of integrating **GitHub Models** into GitHub Actions workflows for intelligent code automation and analysis. Perfect for demonstrating how to leverage GitHub's hosted AI models within your CI/CD pipelines!

---

> 💡 **Feel free to fork and adapt for your own use cases!**

---

Made with ❤️ by the @robertefreeman for @briancl2 .
