# API Documentation

All API calls should be made to `somethingrandom.herokuapp.com`.

## Create a Snippet Box

`POST /snippet`

**Input**

```
{
    "snippet_name" : "unique name for the snippet", <br>
    "snippet_privacy" : true, <br>
    "snippet_expiry" : 5D,  <br>
    "snippet_file" : {
      "file.txt": {
        "contents": "String file contents"
        }
      }
    }
```

**Output**

```
Status: 201 OK
Location: http://http://www.shareboxes.herokuapp.com/snippet/some-id-for-your-snippet

{
  "url": "http://http://www.shareboxes.herokuapp.com/snippet/some-id-for-your-snippet"
  "snippet_id": "1234",
  "snippet_privacy": true,
  "snippet_expiry" : "5D",
}
```
