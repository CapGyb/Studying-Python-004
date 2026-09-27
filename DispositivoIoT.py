class DispositivoIoT:
    def __init__(self, nome: str, bateria: int):
        self.nome: str = nome
        # Garante que a bateria fique estritamente entre 0 e 100
        self.bateria: int = max(0, min(100, bateria))

    def __repr__(self) -> str:
        return f"{self.nome} ({self.bateria}%)"


class HubCentral:
    def __init__(self):
        # Lista vazia de dispositivos conectados
        self.dispositivos: list[DispositivoIoT] = []

    def adicionar_dispositivo(self, dispositivo: DispositivoIoT) -> None:
        """Adiciona um dispositivo à lista de conectados."""
        self.dispositivos.append(dispositivo)

    def relatorio_bateria_baixa(self) -> str:
        """
        Itera sobre os dispositivos conectados e retorna uma string
        com o nome de todos que estão com bateria abaixo de 20%.
        """
        dispositivos_criticos = [
            d.nome for d in self.dispositivos if d.bateria < 20
        ]

        if not dispositivos_criticos:
            return "Nenhum dispositivo com bateria baixa."

        return "Dispositivos com bateria baixa (< 20%): " + ", ".join(dispositivos_criticos)


# Execução do cenário solicitado
if __name__ == "__main__":
    # (d) Instanciando três dispositivos IoT com diferentes níveis de bateria
    sensor_presenca = DispositivoIoT("Sensor de Presença Hall", 15)
    camera_seguranca = DispositivoIoT("Câmera Externa", 85)
    termostato = DispositivoIoT("Termostato Sala", 8)

    # Criando o Hub Central
    hub = HubCentral()

    # Adicionando os dispositivos ao Hub
    hub.adicionar_dispositivo(sensor_presenca)
    hub.adicionar_dispositivo(camera_seguranca)
    hub.adicionar_dispositivo(termostato)

    # Executando e exibindo o relatório
    relatorio = hub.relatorio_bateria_baixa()
    print(relatorio)