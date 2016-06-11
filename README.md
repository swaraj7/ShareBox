## for uploading file <br>
  user has to give input in following format as dictionary with following format <br>
  <br>
    snippet_name: \<unique name for your snippet> <br>
    snippet_format: \<extenssion of your code snippet eg- .py, .cpp, .php etc> <br>
    snippet_privacy: \<choose either from "public" or "private"> <br>
    snippet_expiry_date: \<enter the duration till link will be active><br>
    snippet_text: \<provide you code snippet here><br>
  
## Output <br>
Possible Good API responses <br>
shareboxes.herokuapp.com/id/some-unique-id-for-your-snippet
<br> <br>
Possible Bad API responses <br>
Bad API request, invalid snippet_name <br>
Bad API request, maximum paste file size exceeded <br>
Bad API request, invalid snippet_expire_date <br>
Bad API request, invalid snippet_privacy <br>
Bad API request, invalid snippet_format <br>
<br> <br>



