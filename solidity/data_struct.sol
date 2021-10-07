// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.5.1;
//pragma solidity >=0.7.0 <0.9.0;


contract smart_contract {

    // define non-negative 256 bits int value
    // define a data structure that would allow key-value data type with mapping
    uint256 public people_count = 0;
    mapping(uint => Person) public people;
    
    // define the variable to store the owner of the smart_contract
    address owner;
    
    // check if the sender is the owner and throw an exception in the case
    modifier only_owner() {
        require(msg.sender == owner);
        _;
    }
    
    // define our data structure
    struct Person {
        uint _id;
        string _first_name;
        string _last_name;
    }
    
    
    //function needed to increase people_count, just for internal access only
    function increment_count() internal {
        people_count++;
    }

    // instantiation function
    function add_person(string memory _first_name, string memory _last_name) 
        public 
        only_owner
    {
        increment_count(); 
        people[people_count] = Person(people_count, _first_name, _last_name);
    }
    
    
}
