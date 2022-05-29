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

on:
  workflow_dispatch:


jobs:

  js-check-update-action:
    runs-on: ubuntu-latest
    steps:
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
