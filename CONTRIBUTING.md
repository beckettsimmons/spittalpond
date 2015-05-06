How to Contribute
=================

As with many project on Github we welcome pull requests!

Making Changes
--------------

Fork this project on Github (you will need a Github account), then clone the
repo onto your local machine.

This project somewhat follows the common [Gitflow] branching model. Basically
for you that means you should branch off of develop to create your new feature
branch. Make all of your commits on your new branch then push to your fork and
submit a pull request.

Example workflow:
``` sh
git branch fix-broken-thing origin/develop
git checkout fix-broken-thing
git push origin
```

Try to avoid making commits directly on the master or develop branches.

Pull upstream changes into your fork regularly
----------------------------------------------
As development moves on more commits are made to the main repository. It is
therefore critical that you pull upstream changes from develop into your fork
on a regular basis. Nothing is worse than putting in a days of hard work into a
pull request only to have it rejected because it has diverged too far from
develop.

To pull in upstream changes:
``` sh
git remote add upstream https://github.com/beckettsimmons/spittalpond.git
git fetch upstream develop
```
Check the log to be sure that you actually want the changes, before merging:

``` sh
git log upstream/develop
```
Then merge the changes that you fetched:

``` sh
git merge upstream/develop
```

For more information see [here].

Style
-----

This project loosely follows the python [PEP 8] code style specification.
Please try to follow this as closely as possible, but of course you are the
pragmatic programmer so you make the last call and don't follow the spec
blindly!

Specifically, from PEP 8 be aware of two things: long lines and whitespace
- Please follow the maximum line length convention and limit all lines to **79
  characters**! (80 chars include the, mostly invisible, eol) The only real
  exception to this it when specifically using literals. i.e.  the URLs at the
  bottom of this file, Python tracebacks in documentation, etc.
- Be aware of whitespace. This means both [blank lines] and [inline
  whitespace]. Nobody likes viewing that unnecessary diff that is mostly
  someone being liberal with they spacebar... Speaking of which, let's all just
  use unix line endings as well, cool.

Also, please [appropriately] document your code with any pro-tips and
divine knowledge; in order to spare us all from having to guess/be
confused. Specifically please write [docstrings] in such a way that the Python
`help()` function can be used on it to gather useful, relevant, and concise
information and pro-tips about the function/class/module! Note that we use
[Google style] docstrings in order to auto-generate code documentation with
Sphinx. So it's rather important to follow this convention correctly.

As for commits; make sure that they are logical units with an [appropriate
commit message]. Always `git diff` before you commit to ensure that everything
you changed it what you wanted to change! (Extra whitespace likes to hide
here!)

Other
-----

It might be worthwhile to mention that branches prefixed with `expr/` are
experiment branches. These branches are bending the common practice of Linus
himself; ["Don't expose your crap."] They are only public for test purposes and
will most probably be rebased/deleted without warning! So unless you are
explicitly involved with them, you can safely ignore these branches.


[Gitflow]: <http://nvie.com/posts/a-successful-git-branching-model/>
[here]: <https://help.github.com/articles/configuring-a-remote-for-a-fork/>
[PEP 8]: <https://www.python.org/dev/peps/pep-0008/>
[blank lines]: <https://www.python.org/dev/peps/pep-0008/#blank-lines>
[inline whitespace]: <https://www.python.org/dev/peps/pep-0008/#whitespace-in-expressions-and-statements>
[appropriately]: <http://blog.codinghorror.com/code-tells-you-how-comments-tell-you-why/>
[docstrings]: <https://www.python.org/dev/peps/pep-0008/#documentation-strings]
[Google style]: <http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html>
[appropriate commit message]: <http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html>
["Don't expose your crap."]: <http://www.mail-archive.com/dri-devel@lists.sourceforge.net/msg39091.html>
