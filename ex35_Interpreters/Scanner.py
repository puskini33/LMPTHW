import re
from sys import exit


class Scanner(object):

    def __init__(self, regex_rules: 'list of tuples', text_to_match: list):
        """Algorithm takes as input a set of regex rules and a piece of code and outputs a list of tokens that matches the
        code in the order it is written."""
        self.rules = regex_rules
        self.text_to_match = text_to_match
        self.list_tokens = []  # list of tuples
        self.scan()

    def scan(self):
        """Takes a string and runs the scan on it, creating a list of tokens for later. You should keep
        this string around for people to access later."""
        for line in self.text_to_match:  # taking each line from the code to match
            i = 0
            while i < len(line):  # looping till the end of the string is reached

                token, string, end = self.try_match(i, line)  # i = 3, line = code[0]

                if token:  # if a token is matched
                    i += end  # set the new index to take the unmatched string
                    self.list_tokens.append((token, string, i, end))  # append the found goods
                else:
                    print(f'SyntaxError: Unmatched Regex Token  {line[i:]}  at line:  '
                          f'\n{line}')
                    exit(1)

    def try_match(self, i: int, line: str):
        """Given a list of possible tokens, returns the first one that matches the first token in the list
        and removes it."""
        start = line[i:]  # take the unmatched string
        for regex, token in self.rules:  # for each set regex and token (tuple)
            compiled_regex = re.compile(regex)
            match = compiled_regex.match(start)  # verify to see if the string matches the regex
            if match:  # if a match is found
                begin, end = match.span()  # take the begin and end index
                """ Span returns a tuple containing the (start, end) positions of the match"""
                return token, start[:end], end  # return TOKEN

        return None, start, None

    def match(self, token_id: str) -> list:
        """Given a list of possible tokens, returns the first one that matches the first token in the list
    and removes it."""
        while token_id == 'SPACE':
            self.ignore_ws()

        if token_id != 'SPACE':  # lexical analyser eliminates spaces
            self.ignore_ws()

        try:
            if self.list_tokens[0][0] == token_id:
                removed = self.list_tokens.pop(0)
                return [removed[0], removed[1]]
        except None:
            return 'ERROR'

    def peek(self) -> list or str:
        """Given a list of possible tokens, returns which ones could work with match but does not
        remove it from the list."""
        if not self.done():
            self.ignore_ws()
            return self.list_tokens[0][0]
        else:
            return 'ERROR'

    def ignore_ws(self):
        """Functions pops the INDENT token. The lexical analyser must remove all spaces."""
        while self.list_tokens[0][0] == 'SPACE':
            self.list_tokens.pop(0)

    def skip(self, *what: tuple) -> bool:
        """Function evaluates if first element in the given list of tokens equals the first element
        in the list of tokens of the object. If YES, it returns TRUE, if NOT, it pops the first element and
        tries again, and returns False if also first new element does not match."""
        for x in what:
            if x != 'SPACE':
                self.ignore_ws()

            tok = self.list_tokens[0]
            if tok[0] != x:
                return False
            else:
                self.list_tokens.pop(0)
                return True

    def push(self, rule_token):
        """Pushes a token back on the token stream so that a later peek or match will return it."""
        for i in range(0, len(self.list_tokens)):
            if rule_token[1] == self.list_tokens[i][0]:
                continue
            else:
                self.rules.append(rule_token)

    def done(self):
        return len(self.list_tokens) == 0
