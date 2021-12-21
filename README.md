# Orchest + Meilisearch + PyWebIO + HN

Search HN user comments through a PyWebIO interface backed by a Meilisearch DB

![Fetch HN and load into Meili pipeline](https://pviz.orchest.io/?pipeline=https://github.com/ricklamers/orchest-meilisearch-pywebio-hn/blob/master/load_and_search.orchest)

Import `https://github.com/ricklamers/orchest-meilisearch-pywebio-hn` to your Orchest instance to try it out.

On `Fetch data` you can configure:

```
{
  "all_pages": false,
  "proxy_enabled": true,
  "usernames": [
    "ricklamers"
  ]
}
```

On `Load into Meili` you can configure:
```
{
  "clear_db": true
}
```
