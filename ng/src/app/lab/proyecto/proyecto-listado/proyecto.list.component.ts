import {Component, Input, OnInit} from "@angular/core";
import {ProyectoService} from "../service/proyecto.service";
import {Proyecto} from "../service/proyecto";

@Component({
    selector: "proyecto-list",
    templateUrl: "proyecto.list.component.html",
    providers: [ProyectoService]
})
export class ProyectoListComponent implements OnInit {

    public proyectos: Proyecto[] = [];
    @Input() filtro = "";

    constructor(private _proyectoService: ProyectoService) {

    }

    filtrar() {
        console.log("Controlador filtrando proyectos");
        this._proyectoService.listarProyectosFiltrados(this.filtro).subscribe((proyectos: Proyecto[]) => this.proyectos = proyectos);
    }

    getProyectos() {
        this._proyectoService.getProyectos().subscribe((proyectos: Proyecto[]) => this.proyectos = proyectos);
    }

    ngOnInit(): any {
        this.getProyectos();
    }
}
