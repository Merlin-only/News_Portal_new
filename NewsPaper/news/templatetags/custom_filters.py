from django import template

register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def filter_text():
   variants = ['Блядь', 'mat', 'abc']  # непристойные выражения
   ln = len(variants)
   filtred_text = ''
   string = ''
   pattern = '*'  # чем заменять непристойные выражения
   for i in text:
      string += i
      string2 = string.lower()

      flag = 0
      for j in variants:
         if not string2 in j:
            flag += 1
         if string2 == j:
            filtred_text += pattern * len(string)
            flag -= 1
            string = ''

      if flag == ln:
         filtred_text += string
         string = ''

   if string2 != '' and string2 not in variants:
      filtred_text += string
   elif string2 != '':
      filtred_text += pattern * len(string)

   return filtred_text