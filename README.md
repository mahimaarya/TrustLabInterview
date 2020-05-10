# TrustLabInterview (Mahima Arya)

### Sub-Problem
I chose to create a way for users to report misinformation and hate speech content to trustlab.

### Solution: YouTube Comment Reviewer
My Flask app specifically looks at identifying misinformation and hate speech in YouTube comments. This solution takes a crowdsourcing approach where users visit the YouTube Comment Reviewer site, submit a URL, and sift through the comments. They can mark comments as good or submit them to trustlab for further review. Later, trustlab will be able to see what the users have submitted.

This approach simplifies things for non-technical users, because the only information they would need to provide is a YouTube link.

### Improvements to be Made
1. Functionality: There are gulfs of execution (for example, the "Mark as Good" button doesn't do anything when clicked), so we would want to resolve those to make the website work.
2. Database: The product could be improved with the addition of a database to store which comments are getting marked as good vs. suspicious.
3. YouTube API: With access to the YouTube API, we can use actual comment information.
4. Usability Testing: Doing think-aloud studies with users will tell us which interactions can be improved.
5. Recommendations: Users can get recommendations for YouTube links on the home page in case they don't already have a video that they want to review. Users can also receive recommendations on comments to review based on the number of likes they receive, the number of replies, or the reviews given by other users.
7. Dashboard: A dashboard for trustlab employees to see aggregate information about YouTube comment reviews.

### Product Vision
Instead of a Flask app, a Chrome extension may benefit users. Instead of opening a new page, the effort to submit a review would be reduced, because a comment could be sent to trustlab within the page. I imagine that the UX flow would be the user downloading the Chrome extension, clicking on the 3 dots next to a YouTube comment, and selecting either "trustlab: mark as good" or "trustlab: send for review". When a comment has been marked, the interface would make a border around the comment to signify that it has already been reviewed. With this design, the tradeoff may be that we won't see as many comments that are marked as good, because users may not be motivated to mark them, but this is something we could look into deeper with user research and a competitive analysis.

### Libraries/Packages
Flask installation (for Terminal on Mac):
```
pip3 install flask
```

Requests installation (for Terminal on Mac):
```
pip3 install requests
```

### How to Run the Code
Clone this repository and navigate to the directory.
Run the following commands (for Terminal on Mac):

```
source venv/bin/activate
flask run
```

The website should now be running! On my computer, it was hosted on http://127.0.0.1:5000/, but it may be different on yours.


Thank you!

\- Mahima Arya (mahimaa@andrew.cmu.edu)
