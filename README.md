A RESTful api to store and share your code-snippets among people.


# API Documentation

All API calls should be made to `http://www.shareboxes.herokuapp.com/`.

## Create a Snippet Box

`POST /snippet`

**Input**

```
{
    "snippet_name" : "unique name for the snippet", <br>
    "snippet_privacy" : true, <br>
    "snippet_expiry" : 5D,  <br>
    "snippet_file" : {
      "file.txt" : {
        "contents": "String file contents"
        }
    }
}
```

**Output**

```
Status: 201 OK
Location: http://www.shareboxes.herokuapp.com/snippet/some-id-for-your-snippet

{
  "url": "http://http://www.shareboxes.herokuapp.com/snippet/some-id-for-your-snippet"
  "snippet_id": "1234",
  "snippet_privacy": true,
  "snippet_expiry" : "5D",
}
```

## To access the snippet from link

`GET /snippet/id`

**Input**
``` 
{
    "snippet_id" = 1234
}
```

**Output**
```
Status : 302 Found
Location: http://http://www.shareboxes.herokuapp.com/snippet/some-id-for-your-snippet
{
    "snippet_file" : {
      "file.txt" : {
        "contents": "String file contents"
        }
    }
}
            
            
