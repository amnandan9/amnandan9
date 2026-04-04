# How to Contribute?

_This project is free for contributions from ORG teams, as long as the contributions are made in a way that does not violate the scope defined by the project and its main objective._

1. First create a new branch to start contributing. Follow the [Creating Branches](#creating-branches) instructions.
2. Submit your commits using [Angular Convention](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#-commit-message-format). Follow the [Creating Commits](#creating-commits) instructions.
3. Once the code is ready, open a pull request and fill all the information needed.
4. Make sure your PR meets all requirements:
   - Check if the build is successful
   - Check if all the tests, lint and sonar requirements are passing
   - Check if doesn't add any new `warning`
   - Check if there are any conflicts
   - Attach test evidence to your pull request
5. Ask your colleagues to review your pull request. If necessary send us a message on slack/discord channel.
6. After 1 or more approvals, use the squash strategy to merge to main branch and delete the branch 


## Creating Branches
_Make sure to have an issue on board linked to new branch._ 

Branch naming is as follows:
- `feature/<name>` for new features
- `fix/<name>` for bug fixes or quick fixes
- `release/<name>` for big releases

where:

**name:** `<issue-code>_<summary-name>`
```  
fix/XPT-123_change-request-to-api
 
feat/XPT-321_add-endpoint-to-get-users
```


## Creating Commits

The [Angular Convention](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#-commit-message-format) has a template for commits to make them very descriptive:

```
<type>(<scope>):<short-summary>
```

You can use [commitizen](https://github.com/commitizen/cz-cli) to facilitate the commit message creation.

## Feature Branches
For some bigger features we use the feature branch strategy. A feature branch is a copy of the main codebase, where different developers can work in little pieces of this feature until it is complete.

Basically we start a branch from the main and all the pull request related to this feature use the feature branch as target.

The naming of the feature branches follow the pattern:
- `feature-branch/<name>`

Where:

**\<name\> :** `<issue-code>_<summary-name>`

```
feature-branch/XPT-999_ad-detail-page
```

## :warning: Atention

* New versions will only be generated with commits like `feat`, `fix` and `perf`
* PR can only be merged after approval by one of the team's `code owners`