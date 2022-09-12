from werkzeug.exceptions import HTTPException


class ApplicationException(HTTPException):
    def __init__(
        self,
        app_error_code: any,
        msg: str = None,
        detail: any = None,
        http_error_code: int = None,
    ):
        """
        Construtor.

        - app_error_code: Código do erro da aplicação. Ou pode ser uma
        instância de `AppErrorCode` ou um valor inteiro.
        - msg: Mensagem do erro. SE não for informado e `app_error_code`
        for uma instância de `AppErrorCode` então a sua mensagem será
        utilizada.
        - detail: Detalhe do erro.
        - http_error_code: Código do erro HTTP (valor padrão 500).
        """
        err_code, err_msg = self._read_error_code_msg(app_error_code, msg)
        self.app_error_code = err_code
        self.description = err_msg
        self.detail = detail
        self.code = http_error_code if http_error_code is not None else 500

    @staticmethod
    def _read_error_code_msg(app_error_code, msg):
        err_code = app_error_code
        err_msg = msg
        if err_msg is None:
            err_msg = "Erro interno no servidor"
        return err_code, err_msg