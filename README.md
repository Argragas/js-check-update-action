# js-check-update-action
This action provides the following functionality for GitHub Actions users:
- check if minor updates are available for your dependencies.
- edit package.json file to fix versions.
- push
- send email with package.json and log of yarn-upgrade-minor cmd 
# Usage:

see [action.yml file](action.yml)
```yaml
name: CI

# Controls when the workflow will run
on:
  workflow_dispatch:

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  js-check-update-action:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest

    # Steps represent a sequence of tasks that will be executed as part of the job
    steps:
      # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
      - uses: actions/checkout@v3
      - run: echo 'TOKEN=${{ secrets.TOKEN_APP }}' >> $GITHUB_ENV
      - run: echo 'MAIL_USERNAME=${{ secrets.MAIL_USERNAME }}' >> $GITHUB_ENV
      - run: echo 'MAIL_PASSWORD=${{ secrets.MAIL_PASSWORD }}' >> $GITHUB_ENV
      - run: echo 'MAIL_TO=${{ secrets.MAIL_TO }}' >> $GITHUB_ENV
      - uses: Argragas/js-check-update-action@v1.6
        with:
          TOKEN_APP:  ${{ env.TOKEN }}
          MAIL_USERNAME:  ${{ env.MAIL_USERNAME }}
          MAIL_PASSWORD:  ${{ env.MAIL_PASSWORD }}
          MAIL_TO:  ${{ env.MAIL_TO }}
         
```
         
# License
The scripts and documentation in this project are released under the [MIT License](LICENSE)
