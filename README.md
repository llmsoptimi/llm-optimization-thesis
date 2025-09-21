# Optimizing Large Language Models: A Benchmarking Framework

This repository contains the source code and experimental data for the bachelor's thesis, "Optimizing Large Language Models: Performance, Personalization, and Scalability Analysis." The project provides a comprehensive framework for evaluating and comparing leading LLMs—**ChatGPT-4 Turbo**, **Claude 4 Sonnet**, and **DeepSeek V3**—across various performance and engagement metrics.

## Project Overview

This research addresses critical gaps in the understanding of LLM performance by:
1.  **Linking Performance to Engagement (RQ1):** Systematically measuring core metrics like latency, accuracy, and resource usage and correlating them with user engagement scores in multi-turn, cohesive, and ethical conversational sessions.
2.  **Analyzing Scalability and Privacy (RQ2):** Stress-testing the models with 25 to 200 concurrent users to determine their performance limits and quantifying the significant overhead of integrating a zero-knowledge privacy protocol (EZKL).

The findings show that model selection is highly use-case-dependent, with ChatGPT-4 Turbo excelling as a scalable generalist and Claude 4 Sonnet as a specialist for safety-critical tasks.

## Features

* **Standardized API Client:** A universal client in `src/` to interact uniformly with different LLM providers.
* **Automated Benchmarking:** Scripts in `experiments/` to run performance tests for latency, accuracy, and resource utilization.
* **Scalability Testing:** A Locust-based framework to simulate concurrent user load and measure throughput, error rates, and latency.
* **Data-Driven Reporting:** Scripts to process raw experimental data and generate insightful plots and visualizations.
* **Reproducible Environment:** A `Dockerfile` to ensure a consistent and replicable testing environment.

## 📂 Repository Structure

The repository is organized to separate source code, data, and experiments, ensuring clarity and ease of navigation.
