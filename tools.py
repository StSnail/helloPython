# 下划线转驼峰命名
# 空行结束
def underline_to_camel_case_naming():
    print("input:")

    lines = ''
    for line in iter(input, ''):  # 输入为空行，表示输入结束
        lines += convert_word_underline_to_camel_case(line) + '\n'
    print(lines)


def convert_word_underline_to_camel_case(word):
    underline = '_'  # 下划线
    chars = list(word)  # 字符串转列表
    is_need_to_upper = False  # 是否需要转大写
    for i in range(0, len(chars)):
        if is_need_to_upper:
            chars[i] = chars[i].upper()
            is_need_to_upper = False
        elif chars[i] == underline:
            is_need_to_upper = True

    new_word = ''.join(chars)
    # 去掉下划线
    return new_word.replace(underline, '')


if __name__ == '__main__':
    underline_to_camel_case_naming()
