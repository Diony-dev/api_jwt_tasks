class Tarea:
    def __init__(self, _id, titulo, descripcion, estado, id_usuario):
        self._id = _id if _id else None
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
        self.id_usuario = id_usuario
        
    def to_dict(self):
        return {
            'id': str(self._id) if self._id else None,
            'titulo': self.titulo,
            'descripcion': self.descripcion,
            'estado': self.estado,
            'id_usuario': str(self.id_usuario) if self.id_usuario else None
        }