🎉✨ Celebrate Contributors
---
This is a GitHub Action for celebrating contributors. The workflow collects all of the contributors for the repository it is within. It then creates a table of contributors and a graph of contributions by contributor. All of this will be stored within [CONTRIBUTORS.md](CONTRIBUTORS.md).

Inspired by: [all-contributors](https://github.com/all-contributors/all-contributors)

Created for: [DEV hackathon](https://dev.to/devteam/announcing-the-github-dev-2023-hackathon-4ocn)

🧑‍💻 Usage
---
To ensure the Action is able to write to the repository. You must enable write permissions in the repository settings. You can do this my navigating to Settings -> Actions -> General -> Workflow Permissions and select 'Read and write permissions'. Once saved the Action will work as intended!

The Action is configured to be reusable. Please, feel free to use it in your repository!

```yaml
celebrate-contributors-call:
  uses: slouchd/celebrate-contributors/.github/workflows/celebrate-contributors.yml@main
```

🪪 License
---
MIT License