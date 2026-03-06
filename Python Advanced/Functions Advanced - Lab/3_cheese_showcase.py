def sorting_cheeses(**cheese_info):
    result = ''
    sorted_cheeses = sorted(cheese_info.items(), key=lambda x: (-len(x[1]),x[0]))
    for cheese,pieces in sorted_cheeses:
        result += f'{cheese}\n' + '\n'.join(str(p) for p in sorted(pieces, reverse=True)) + '\n'

    return result.strip()



