# Generate and Apply Patches

Sometimes you need to change code on a machine from which you cannot push to the repo. You're ready to copy/paste what `diff` outputs to your local working copy.

**1\. Generate the patch:**
```
git diff > some-changes.patch
```

**2\. Apply the diff:**

Then copy this patch to your local machine, and apply it to your local working copy with:
```
git apply /path/to/some-changes.patch
```

The changes are now in your working copy and ready to be staged/commit/pushed