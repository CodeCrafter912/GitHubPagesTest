<p align="center">
 <h1 align="center"> - GitHubPagesTest - </h1>
</p>

<p align="center">
  <a href="https://github.com/CodeCrafter912/GitHubPagesTest/actions/workflows/release.yml"><img src="https://github.com/CodeCrafter912/GitHubPagesTest/actions/workflows/release.yml/badge.svg" /></a>
  <img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" />
</p>

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

# Index of /
Files in this directory:
- 📁 [dists/](dists)
- 📁 [pool/](pool)
- 🗒 [pub.gpg](pub.gpg)
