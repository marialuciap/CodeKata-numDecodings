Use this repository as a template to create other battles.
The files to modify to create a new battle are:

- main.py, where you can specify the outline of the battle for which students will need to provide the solution through the implementation of the indicated function (in the example, mySum).
- code_kata_test.py, where the test cases verifying the correct implementation of the function required by the battle should be specified. Students will earn points in proportion to the number of test cases passed (in the example, test1, test2, and test3).
- .github\workflows\python-app.yml, replace at line 46 instead of <github-main-account>, the name of the account currently used to upload the battle code, from which users will fork. Instead of <zip-to-upload-name>, use the name of the zip file uploaded by the educator (without extension). Instead of <smee-channel-address>, use the address of the proxy to which the webhook will send the payload containing the performance result, with each push to the repository forked by the user.
