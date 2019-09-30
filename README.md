# Master branch protector

This is a simple web service that listens for organization events to know when a repository has been created. When a repository is created, the protection on master branch is automatically enabled, and an issue is created in the repository where a designated person is notified with a @mention that outlines the protections that were added.

