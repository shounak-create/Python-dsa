def validparenthesis(arr):
    # openings=['(','{','[']
    # closings=[')','}',']']
    check = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    include = []

    if arr and len(arr) % 2 == 0:
        for i in arr:

            # closing bracket
            if i in check.keys():

                # if stack is empty
                if not include:
                    return False

                store = check[i]

                # compare with top
                if store == include[-1]:
                    include.pop()
                else:
                    return False

            # opening bracket
            else:
                include.append(i)

        # after loop stack should be empty
        if len(include) == 0:
            return "list has valid parenthesis"
        else:
            return False

    return False

arr = "({[]})"
print(validparenthesis(arr))