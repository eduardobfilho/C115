import socket
import json

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))

    # Recebe as questões do servidor
    questions = json.loads(client.recv(1024).decode())

    responses = []
    for i, q in enumerate(questions):
        print(f"\n{i + 1}. {q['question']}")
        for idx, option in enumerate(q["options"]):
            print(f"{idx}. {option}")
        
        answer = int(input("Sua resposta (número): "))
        responses.append(answer)

    # Envia as respostas para o servidor
    client.sendall(json.dumps(responses).encode())

    # Recebe o resultado do servidor
    result = json.loads(client.recv(1024).decode())

    print("\nResultado:")
    for item in result["details"]:
        status = "Correto!" if item["correct"] else "Errado!"
        print(f"{item['question']} - {status}")

    print(f"\nPontuação final: {result['score']} de {len(questions)}")

    client.close()

if __name__ == "__main__":
    start_client()
