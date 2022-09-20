# Checklist for evaluating your project's git process
Your project can define your own git process. It does not have to follow the simple two-level branching described in [GitBranchingBasics.pdf](GitBranchingBasics.pdf). Nor the four-level branching from https://nvie.com/posts/a-successful-git-branching-model/  

But, when you define and follow your team's own process, you might want to check certain aspects. Does it tackle these goals or challenges?

Below each goal there are actions/aspects from GitBranchingBasics that work on those goals.

<hr />

## Merging of everybody's work to the common product is conflict-free, risk-free and doesn't always require the most advanced programmer's check

1. Do git pull several times while, reading, planning, and right before new changes
1. Publish* changes to common files, common folder structure, and create the needed new files asap so that there is a place for git to add new changes
1. Do microedits (especially in school where we don't need no product running in "production environment") the faster you share skills to others, the faster others can join in reviewing and developing. 
1. Separate your thinking from Scrum Definition of Done. Don't 
mix Scrum and git version management. Publish partial results, as long as it does not break anything.

(* Publish = all steps through review and merge to remote main) 

## Developers know who is doing what on the project, right now (Even without looking at Scrum board)

1. do the push --set-upstream immediately, even before work, so that your dev branch is visible to others
1. use a good descriptive name for the worked on things, starting
from the corner of the product, e.g. user role or app view,
then more towards details: product-listAll-add-filtering
1. add the developer names at the end to tell whom to ask/contact
product-listAll-add-filtering-juhani-liisa
1. delete the branch immediately after the merge to communicate to others the active work is finished. You can open branch with exactly same name by hitting arrow up and finding the commands from history. No need to keep the branch.
1. Join others by adding your review (students review the work, teacher only sometimes if needed at night or so)

<hr />
