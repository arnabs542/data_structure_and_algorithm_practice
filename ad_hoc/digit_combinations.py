'''
/*
                            ''
        'A'                 'B'                 'C'
  'AD'  'AE'  'AF'    'BD'  'BE'  'BF'    'CD'  'CE'  'CF'
*/



    def phone_permute_list(digits, mapping):
      if len(digits) == 0:
        return ['']
      else:
        result = []
        for x in phone_permute_list(digits[1:], mapping):
          for y in mapping[digits[0]]:
            result.append(y + x)
        return result

    ['AD', 'BD', 'CD', 'AE', 'BE', 'CE', 'AF', 'BF', 'CF']
        [     'D',             'E',              'F']
                             ['']
    "12345"
    ['AD', 'BD', 'CD', 'AE', 'BE', 'CE', 'AF', 'BF', 'CF']
    ...
    -> map^n

    def phone_permute_iter(digits):
      results = ['']
        // [     'D',             'E',              'F']
      nxt_result = []
        // ['AD', 'BD', 'CD', 'AE', 'BE', 'CE', 'AF', 'BF', 'CF']
      while len(digits) > 0:
        nxt = digits[0]
        for r in results:
          for char in mapping[digits[0]]:
            nxt_result.append(r + char)

        digits = digits[1:]
        results = nxt_result
        nxt_result = []

      return results

void phoneNumberToString(string prefix, string digits, map<char, vector<char> > &mapping) {

    // if digits is length 0
    if(digits.size() == 0) // ("A", "23", mapping)
    {
        cout << prefix << endl;
        return;
    }

    // for each character that the first char of digits is mapped to
    //
    for(int i = 0; i < mapping[digits[0]].size(); ++i) // ("A", "23", mapping)
    {
        string next_prefix = prefix + mapping[digits[0]][i];
        string next_digits(digits, 1); // digits[1:] -> 23
        phoneNumberToString(next_prefix, next_digits, mapping); //
    }
    return;
}


void phoneNumberToString(string digits, map<char, vector<char> > &mapping) {

    phoneNumberToString("", digits, mapping);
    return;
}

int main()
{

    // Define your mapping here
    // mapping = {'1': ['A', 'B', 'C'], '2': ['D', 'E', 'F'], '3': ['G', 'H', 'I'], '4': ['J', 'K', 'L'] }

    map<char, vector<char> > mapping;

    mapping['1'] = {'A', 'B', 'C'};
    mapping['2'] = {'D', 'E', 'F'};
    mapping['3'] = {'G', 'H', 'I'};

    phoneNumberToString("123", mapping);

    return 0;
}

'''
def phoneNumberToString(digits, mapping):
    #
    # Write your code here.
    #
    for digit in digits:
        if digit in mapping:
            for letter in mapping[digit]:
                print(digit + letter)
            print()

d = {'1': ['A', 'B', 'C'], '2': ['D', 'E', 'F'], '3': ['G', 'H', 'I'], '4': ['J', 'K', 'L']}
phoneNumberToString("12", d)
