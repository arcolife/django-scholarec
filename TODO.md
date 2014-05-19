TODO
===

- integrate django-social-auth 
  - [x] integrate Twitter0
  - [x] integrate Facebook 
    - [x] resolve invalid App Id 
  - [ ] Integrate Fedora (FAS) 
    - [ ] resolve no redirect url
  - [x] integrate Github 
    - [x] resolve no such page error 
  - [x] integrate Persona (Mozilla) 
  - [ ] integrate Google 
    - [x] Google OpenId 
    - [ ] Google OAuth1 
      - [] Reset permissions (currently, profile, email, google drive)
    - [ ] Google OAuth2 
      -	[ ] Resolve Error: invalid_client. Bad request.
  - [x] integrate sign-in page
  - [x] integrate session trackers / cookies
  - [ ] resolve no disconnect allowed issue
- [x] Connect Social Auth to HomePage 
- [x] Add query_parse statements to models.py
- [x] Display JSON data file in browser
- [x] Refactor HTML code
- [x] Refine database and replace mockup viz
- [x] Integrate Search URL box with DB

***

- [ ] Add scroll down arrow Gif's to homepage
- [x] Refactor /done UI (similar to /login)
- [x] add search history expand-collapse column to /results
- [x] integrate search history
- [x] add pagination UI controls to /results 
- [x] intergrate pagination 
- [x] add labels/keywords panel display on /results
- [x] integrate documents labels / keywords
- [x] Add star and heart icons to papers
- [x] integrate recommender to /results
- [ ] add visualizations page/controls/options to UI on /results
- [ ] integrate visualizations
- [ ] Add carousel (slideshow) to homepage / HINT: bootstrap carousel.js
- [ ] enable semantic search /NLP
- [ ] Integrate Collections:
    - [x] Integrate add_collection() and get_collection() with 
      	  the heart icons for collection
    - [ ] Enhance UX
    - [x] Integrate get_collection()
    - [x] Display Collections in panel
- [ ] Integrate ratings / stars:
    - [ ] Change stars as per request (integrate get_ratings() from control.py)
    - [x] Integrate stars in UI, connect stars to backend.
- [x] Integrate User's favorites.