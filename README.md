# GitHubPagesTest

[![Build and Deploy](https://github.com/CodeCrafter912/GitHubPagesTest/actions/workflows/release.yml/badge.svg)](https://github.com/CodeCrafter912/GitHubPagesTest/actions/workflows/release.yml)

This is an example demonstrating how to host a custom Debian repository using GitHub pages.

# Setup
To use the repository, please follow these steps:
1. Import key:
```bash
wget -qO - "https://codecrafter912.github.io/GitHubPagesTest/pub.gpg" | sudo apt-key add -
```
2. Add repo:
```bash
echo "deb https://codecrafter912.github.io/GitHubPagesTest bionic main" > /etc/apt/sources.list.d/GitHubPagesTest.list
```
3. Apt update
```bash
apt update
```
