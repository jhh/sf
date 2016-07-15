# Stryke Force Git Repository

The proposed layout is something like (names are for illustration, TBD):

    strykeforce2767
      |_robot (this is the repo)
          |_ docs (these are top-level dirs in repo)
          |_ driverstation
          |_ tools
            |_ grapher
            |_ bdc_comm
          |_ control
          |_ vision
          |_ camera
          |_ shared
          |_ scripts
          |_ vendor (location for 3rd-party code)
            |_ wpilib (these are not committed)
      |_ website
        |_...
      |_ docs (clone of our public docs repo on github)
        |_ docs
        |_ talks
      |_ wpilib (if we have to fork for a bug)

- We use a single repository for each group of related projects.
- We will use the `master` branch for production releases and the `dev` branch for development.
- Whenever practical, small `feature` branches should be used and merged to development when done.
- The repo manager is responsible for merging tested and reviewed releases from the `dev` branch to the `master` branch.
- Releases will be tagged using a modified version of [Semantic Versioning 2.0][semver]. Our version format will be `YEAR.MAJOR.MINOR.PATCH`, for example 2017.1.1.12.
  - YEAR: the current competition year.
  - MAJOR: increment version when we make incompatible API changes.
  - MINOR: increment version when we add functionality in a backwards-compatible manner.
  - PATCH: increment version when we make backwards-compatible bug fixes.
- 3rd-party code has a standard location in the directory structure but is not uploaded to repo.

[semver]: http://semver.org/
