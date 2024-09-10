# Changing Git Configurations

This guide explains how to change your Git configuration settings, both globally and locally.

## Table of Contents
- [Changing Global Git Configuration](#changing-global-git-configuration)
  - [Set Global User Name](#set-global-user-name)
  - [Set Global User Email](#set-global-user-email)
- [Verifying Changes](#verifying-changes)
- [Understanding Global vs Local Git Configurations](#understanding-global-vs-local-git-configurations)

## Changing Global Git Configuration

To change your global Git configuration to use the name "yy" and email "yy@xx.com", follow these steps:

### Set Global User Name

To set the global user name:

```bash
git config --global user.name "yy"
```

### Set Global User Email

To set the global user email:

```bash
git config --global user.email "yy@xx.com"
```

## Verifying Changes

After running these commands, you can verify the changes by running:

```bash
git config --global user.name
git config --global user.email
```

These commands should now display "yy" and "yy@xx.com" respectively.

## Understanding Global vs Local Git Configurations

Git configurations can be set at three levels:

1. System level: Applies to all users on the system and all their repositories.
2. Global level: Applies to all repositories for the current user.
3. Local level: Applies only to the current repository.

When you use the `--global` flag, you're setting configurations that apply to all of your Git repositories on your machine. Local configurations (set without the `--global` flag) override global settings for a specific repository.

If you've set values locally for a specific repository without the `--global` flag, those settings will only apply to that particular repository. The global settings we've changed in this guide will apply to all other repositories unless overridden by local settings.

To set local configurations for a specific repository, you would use the same commands without the `--global` flag while in that repository's directory.
