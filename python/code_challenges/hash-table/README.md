# Hashtables
<!-- Short summary or background information -->
Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.

## Challenge
<!-- Description of the challenge -->
mplement a Hashtable Class with the following methods:
* add
* get
* contain
* hash

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Big O:
* Time: O(1).
* space: O(1).
## API
<!-- Description of each method publicly available in each of your hashtable -->
* Add method will take a key and value and add them to the bucket.
* hash will take the key and make a new index from it.
* Get method will take a key and return the value crossbonding to the key in the hashtable
* contains will take a key and return a boolean indication if the key exist or not.