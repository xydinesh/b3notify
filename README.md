# b3notify
Bitbucket Build Status Notifier (b3notify), is a command line client that can be use to notify build status back to bitbucket server. There is a jenkins plugin for bitbucket cloud deployment which requires OAuth credentials. This library focus on bibucket server and uses basic authentication.

b3notify follows REST API for [updating bitbucket build status](https://developer.atlassian.com/bitbucket/server/docs/latest/how-tos/updating-build-status-for-commits.html)

## Configuration

  Save following content in ~/.b3notifyrc or .b3notifyrc

  ```
  [default]
  url = 'https://<bitbucket-base-url>/rest/build-status/1.0/commits/'
  username = 'builder'
  password = 'builder-password'
  ```
  
## Usage

### Success
  ```
  b3notify --success --commit 'commit-hash' --build-url 'url for current build' --key 'build-key' --name 'build-tag'
  ```
  
  with jenkins 
  
  ```
  b3notify --success --commit $GIT_COMMIT --build-url $BUILD_URL --key $BUILD_TAG --name $BUILD_DISPLAY_NAME
  ```
  
### Failure
 
  with jenkins 
  
  ```
  b3notify --fail --commit $GIT_COMMIT --build-url $BUILD_URL --key $BUILD_TAG --name $BUILD_DISPLAY_NAME
  ```
  
### In progress
 
  with jenkins 
  
  ```
  b3notify --progress --commit $GIT_COMMIT --build-url $BUILD_URL --key $BUILD_TAG --name $BUILD_DISPLAY_NAME
  ```
