# Parallel code scanning with CodeQL

If you have a large repository containing various independent projects (a
"monorepo"), the time taken to scan your code with CodeQL can be significantly
reduced by splitting the scanning work into various parallel jobs which will
individually analyze only a subset of the files in the repository.

This repository contains an example of a GitHub Actions
[workflow](.github/workflows/code-scanning.yml) which does precisely
that. The strategy implemented here works however only for the interpreted
languages supported by CodeQL (e.g. Python and JavaScript). As a first step in
this workflow, all non-hidden subdirectories under the repository's root
directory are detected; parallel code scanning jobs are then dynamically
generated for each subdirectory containing a software project. The
subdirectories [`project-1`](./project-1), [`project-2`](./project-2) and
[`project-3`](./project-3) here represent three independent software projects
inside the repository, each one of which will be scanned in a dedicated job
(i.e., three jobs will be generated in total). Adding a new software project to
this repository (e.g. `project-4`) requires no changes to the workflow file as a
dedicated code scanning job will be automatically generated for it when the
workflow is executed.

If the workflow is triggered by a pull request the list of sub-directories that 
will be scanned will be limited to the subdirectories that contain changes. The 
changes are based on a `git diff` between the base and head repositories specified
in the pull request.  

This strategy is possible because GitHub Actions workflows accept JSON input to
define a job matrix, and  the JSON contents can be generated during the
workflow's execution. In other words, the job matrix can be defined dynamically.

**NOTE**: The approach presented here must be taken with care as accidentally
splitting a software component in this manner may reduce CodeQL's ability to
recognize certain types of vulnerabilities in that component. For instance, it
may not be able to entirely map how data flows inside the component and
therefore miss possible attacks against it. Please make sure you understand the
general capabilities of CodeQL before doing this.

## Answers to common questions

**1.** _Every code scanning job checks out the repository in parallel. If a
change is made to the repository during that time (e.g. a subdirectory is added
or removed, or a file in a pre-existing subdirectory is modified), you
essentially have a race condition which is not being properly handled._

This situation will not occur because the
[`actions/checkout`](https://github.com/actions/checkout/) action only fetches a
single commit by default, for the ref/SHA which triggered the workflow. This
implies that the same code snapshot will be checked out in all jobs triggered
inside the [`Code scanning`](.github/workflows/code-scanning.yml) workflow.

If the amount of data fetched in each checkout step is large, you may get a
performance improvement by generating an artifact containing the code in the
very first job which is executed in the workflow and then consuming that
artifact in all downstream jobs. The
[`actions/upload-artifact`](https://github.com/actions/upload-artifact) and
[`actions/download-artifact`](https://github.com/actions/download-artifact)
actions will help you accomplish this.
