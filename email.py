class Email:
    def __init__(self, content: str) -> str:
        if not isinstance(content, str):
            raise TypeError("Not a valid string")
        if "@" not in content:
            raise TypeError("Does not have an '@' sign")
        
        # Ends with .com/.edu/.net/.org
        # TLD -> Top Level Domain, which is com/org/net
        valid_tlds: list[str] = [".com", ".edu", ".net", ".org"] 
        tld = content[-4:]
        if tld not in valid_tlds:
            raise TypeError("Invalid TLD")
        
        # Check for domain (stuff between @ and .com)
        domain_start = content.find("@")+1
        domain = content[at_sign_index:-4]
        if domain == "":
            raise TypeError("Invalid Domain")
        
        # Check for content before @
        if content.find("@") == 0:
            raise TypeError("Invalid username")

        self.content = content
    

    def __str__(self) -> str:
        return self.content
