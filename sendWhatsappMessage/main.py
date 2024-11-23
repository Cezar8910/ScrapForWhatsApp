import pywhatkit
import time
import datetime
import gspread
""" import httpx
import asyncio """


# async def check_contact(number):
#    try:
#        url = "https://api.ultramsg.com/instance85049/contacts/check"
#
#        querystring = {
#            "token": "p0xcmke19gcbmuqr",
#            "chatId": f"+55{number}@c.us",
#            "nocache": ""
#        }
#
#        headers = {'content-type': 'application/x-www-form-urlencoded'}
#
#        async with httpx.AsyncClient() as client:
#            response = await client.get(url, headers=headers, params=querystring)
#        response_json = response.json()
#        print(response_json['status'])
#        return response_json['status'] == "valid"
#    except:
#        print("error in check_contact")
#        return False

def check_number(number):
    try:
        print(number)
        if (len(number[6:15]) >= 9):
            return True
        return False
    except:
        return False


def main():
    gc = gspread.service_account()
    sh = gc.open("Controle_Escolas")
    worksheet = sh.get_worksheet(0)

    idx = 2043

    while True:
        try:

            values_list = worksheet.row_values(idx)
            time.sleep(2)
            print(values_list)

            if not values_list[9] and values_list[13] == "Cezar":
                print(f"enviado para: {values_list[1]}")


                minute_current = datetime.datetime.now().minute
                hour_current = datetime.datetime.now().hour

                number = values_list[4].replace(" ", "").replace(

                    "(", "").replace(")", "").replace("-", "")
                print(f"number: {number}")
                # number_valid = await check_contact(number)
                number_valid = check_number(values_list[4])
                print(f"number_valid: {number_valid}")
#                if (not number_valid):
#                    worksheet.update_cell(idx, 11, "Número não existe")
#                    time.sleep(5)
#
                if (number_valid):
                    print("inside")
                    # Send a WhatsApp Message to a Contact at 1:30 PM
                    pywhatkit.sendwhatmsg(
                        f"+55{number}", f"Olá, {values_list[1]}. Tudo bem?😁\n\nSou o Cezar Galvão, do time da Tangram Educação Financeira. Estou com uma boa proposta que acredito ser muito valiosa para você. Posso enviar uma mensagem explicando os detalhes?", hour_current, minute_current+1)
                    time.sleep(5)
                    worksheet.update_cell(
                        idx, 10, "1.1 - Prospecção e Qualificação")
                    time.sleep(5)

            idx += 1

        except:
            time.sleep(5)
            print("error")
            idx += 1
            continue


main()


# with open(file, mode='r', encoding='utf-8') as csv_file:
#    csv_reader = csv.reader(csv_file)
#    count_run_total = 20
#    count_run_current = 1
#
#    for row in csv_reader:
#        minute_current = datetime.datetime.now().minute
#        hour_current = datetime.datetime.now().hour
#
#        print(row[3])
#
#        number = row[3].replace(" ", "").replace(
#            "(", "").replace(")", "").replace("-", "")
#
#        if (number.split("9")[0] == "81" or number.split("9")[0] == "87"):
#
#            # Send a WhatsApp Message to a Contact at 1:30 PM
#            pywhatkit.sendwhatmsg(
#                f"+55{number}", f"Olá, {row[0]}. Tudo bem?😁\n\nSou o Esdras Albino, do time da Tangram Educação Financeira. Estou com uma boa proposta que acredito ser muito valiosa #para você. Posso enviar uma mensagem explicando os detalhes?", hour_current, minute_current+2)
#            time.sleep(5)
#            count_run_current += 1
#        if (count_run_current == count_run_total):
#            break
# break