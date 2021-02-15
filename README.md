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

This strategy is possible because GitHub Actions workflows accept JSON input to
define a job matrix, and  the JSON contents can be generated during the
workflow's execution. In other words, the job matrix can be defined dynamically.

**NOTE**: The approach presented here must be taken with care as accidentally
splitting a software component in this manner may reduce CodeQL's ability to
recognize certain types of vulnerabilities in that component. For instance, it
may not be able to entirely map how data flows inside the component and
therefore miss possible attacks against it. Please make sure you understand the
general capabilities of CodeQL before doing this.
