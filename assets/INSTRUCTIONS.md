# How to Update Profile Text

If you ever need to change the heading text, your bio text, or the scrolling transitions:

1. Open `generate_assets.py` in your code editor.
2. Scroll to the bottom of the script. You will see neatly arranged strings containing your text (like `"Hi, I'm Nandan A M"`, `"TECHNOLOGIES"`, etc). 
3. Modify the text inside the quotation marks to whatever you desire.
4. Run the script using Python:
   ```bash
   python generate_assets.py
   ```
5. Commit and push your code. The updated scalable graphics will instantly appear in your GitHub profile exactly formatted to your green/black theme!

---

# How to Reuse This Profile (For Other Users)

If you have cloned or forked this repository and want to use this gorgeous cyberpunk theme for your own GitHub profile, follow these simple steps to swap the data to your own account:

### 1. Update the GitHub Action Workflow
Open the `.github/workflows/update-assets.yml` file. You need to replace every instance of `amnandan9` with your own GitHub Username.

```yaml
# In update-assets.yml, update the curl links and the space shooter command:

# Change this:
curl -sLf "https://github-readme-stats-eight-theta.vercel.app/api?username=amnandan9...

# To this:
curl -sLf "https://github-readme-stats-eight-theta.vercel.app/api?username=YOUR_USERNAME...

# And change the space shooter command:
gh-space-shooter YOUR_USERNAME \
  --output assets/space-shooter.gif \
  --strategy random
```

### 2. Update the Python Scripts
Open `gen_trophies.py` and modify the username variable at the very top:
```python
# In gen_trophies.py
USERNAME  = "YOUR_USERNAME"
```

### 3. Update the README links
Finally, open `README.md` and ensure any hyperlinks pointing to the profile are redirecting to yours:
```html
<!-- Change this: -->
<a href="https://github.com/amnandan9">

<!-- To this: -->
<a href="https://github.com/YOUR_USERNAME">
```

### 4. Let it Run!
Commit your changes and push them to your repository. The GitHub Actions workflow will instantly wake up, fetch all of your stats, your streaks, and your commits, and dynamically redraw all the SVGs and the Space Shooter GIF to match your timeline!
