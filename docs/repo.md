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
          |_shared
          |_vendor (location for 3rd-party code)
            |_wpilib (these are not committed)
      |_ website
        |_...
      |_ docs (clone of our public docs repo on github)
        |_ docs
        |_ talks

- We use a single repository for each group of related projects.
- We will use the `master` branch for production releases and the `dev` branch for development.
- Whenever practical, small `feature` branches should be used and merged to development when done.
- The repo manager is responsible for merging tested and reviewed releases from the `dev` branch to the `master` branch.
- Releases will be tagged using [Semantic Versioning 2.0][semver].
- 3rd-party code has a standard location in the directory structure but is not uploaded to repo.

[semver]: http://semver.org/
