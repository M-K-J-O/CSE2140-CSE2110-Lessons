# CSE 2140 Notes

## Version Control Systems     

Version control systems are a category of software tools that help record changes to files by keeping track of modifications done to the code. There are many systems including GIT, Subversion, Mercurial, and Microsoft Team Foundation Version. 

Version Control also provides a framework for _external documentation_, where each commit documents what changes were made from the previous versions of code. In addition, it provides documentation files such as README.md within the project folder

Version control contributes to _change management_ as data is not lost when personnel leave the project and new personnel have documentation about the project. 

When a project is ready for publishing the version control system can package the current project and release it. Release schedules vary depending on the project. THey can either be time-based (such as Microsoft's Update-Tuesday) or feature-based (such as video game being released with the "core" game and downloadable content, DKC, available afterwards). 

### Git and Git Repositories 

Git is a version control system (VCS) that tracks changes to source code. Git repositories are the online storage of the project code, which must be versioned in Git.

(Git and Git Repos are __Not__ on any exams)

Cloning a repository takes a copy of the Git repository and places it onto the local computer. The clone also has all version and branches of the repository .

To create a new version of the source code in Git, the new changes must be __committed__ to Git to save a local version of the changes .

To synchronize the local changes to the online repository, the local committed version must be __PUSHED__ to the online repository.
*NOTE: A user can have multiple commits of a project before pushing the changes to the git repository .

To synchronize changes to the online repository locally, the online must be __pulled__ to the local computer. 

*NOTE Its best practice to pull changes to a local repository before adding additional changes. if a pull is not first done, there may be conflict when trying to synchronize afterwards. 

There are additional features such as collaboration, restoring previous version, and branching that are covered in CS30.

## Computing Science 10 Review 
### Variables 

Variables are a tool to sore data and call that data at a later part of the program. When naming variables, there are different formats such as snake)case. kebab-case, camelCase, PascalCase, lowercase, and UPPERCASE.

#### When naming variables 

1. The name of the variable should be descriptive of the content it is storing. 
2. The name of the variable can only have letters, numbers, underscores, and dashes. 
3. The name of the variable cannot start with a number.

### Primitive Data Types

Data is stored in various types so that the programs can interact with them based on their data type

1. _Strings of characters_ - Store text characters
2. _integers_ - these store non decimal numbers
3. _floats(ing point numbers) - store a decimal number
4. _Boolean_ - Store True or False

### Mathematical operaters 

All Programming languages include basic arithmetic. Common calculations in addition(+), subtraction (-), Multiplication (*), division (/), floor/integer division(//), modulus (%).
*Division will always return a floating point number, while floor division will always return an integer. 

### Comparing Numbers
* ">" - Greater Than
* "<" - Less Than
* ">=" - Greater Than or equal to
* "<=" - Lesser Than or equal to
* "==" - Equals
* "!=" - Not Equals

## Conditional Statements 
Conditional statements separate parts of the program code so that if a specific condition is met. only a portion of the code runs. The condition must result in a True or False (Boolean) statement that determines whether the True section or the False section of the conditional statement runs. 

## Contractions
Contractions are a common English term where two words come are combined to make a single word with both neabubgs (I,e. do not don't). In Python, there are two cinnib cibtractuibsL decusuibs abd accynulation (counting)

### Accumulation 
```python
NUMBER = 0 

NUMBER = NUMBER + 1
```