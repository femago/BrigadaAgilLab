import {Component, Input, OnInit} from "@angular/core";
import {Protocolo} from "../service/protocolo";
import {ProtocoloService} from "../service/protocolo.service";
import {LabelsService} from "../../labels.service";


@Component({
    selector: "protocolo-lista",
    templateUrl: "./protocolo-lista.component.html",
    providers: [LabelsService, ProtocoloService]
})
export class ProtocoloListaComponent implements OnInit {

    public protocolos: Protocolo[] = [];
    @Input() nombre = "";
    @Input() fuente: string;
    _: {};

    constructor(private _protocoloService: ProtocoloService, private _labelsService: LabelsService) {
        this._ = _labelsService.getLabels();
    }

    listarProtocolos() {
        if (this.fuente != null) {
            this._protocoloService.listarProtocolosFiltradosEnExperimentoPorNombre(this.fuente, this.nombre)
                .subscribe((protocolos: Protocolo[]) => this.protocolos = protocolos);
        } else {
            if (this.nombre !== "") {
                this._protocoloService.listarProtocolosFiltradosNombre(this.nombre)
                    .subscribe((protocolos: Protocolo[]) => this.protocolos = protocolos);
            } else {
                this._protocoloService.listarProtocolos()
                    .subscribe((protocolos: Protocolo[]) => this.protocolos = protocolos);
            }
        }
    }

    keyup() {
        this.listarProtocolos();
    }

    getProtocolos() {
        this._protocoloService.listarProtocolos().subscribe((protocolos: Protocolo[]) => this.protocolos = protocolos);
    }

    ngOnInit() {
        this.getProtocolos();
    }
}
