<template>
    <div>
        <new-server-modal
            @close="toggleNewServerModal()"
            @addServer="(server) => { this.$emit('addServer', server); }">
        </new-server-modal>

        <remove-server-modal
            @close="toggleRemoveServerModal()"
            @removeServer="removeServer">
        </remove-server-modal>

        <div class="back">
            <span class="clickable" @click="configurations.showConfigurations = false">
                <span class="clickable glyphicon glyphicon-arrow-left"></span>
            </span>
        </div>
        <div align="center" class="title"></div>
        <div class="content" align="center">
            <table v-if="!empty" class="table table-width table-bordered table-striped table-background">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Server</th>
                        <th>Status</th>
                        <th>Turn On/Off</th>
                        <th class="small-column">Remove</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(server, index) in servers" :key="index">
                        <th>{{index+1}}</th>
                        <th>{{server.name}}</th>
                        <th class="capitalize" :class="{ 'text-green': server.active && server.status == 'green',
                                                           'text-yellow': server.active && server.status == 'yellow',
                                                           'text-red': server.active && server.status == 'red',
                                                           'text-black': !server.active }">
                            {{ server.active ? 'Collecting - ' + server.status : 'Not Collecting' }}</th>
                        <th style="padding-left: 39px" class="small-column">
                            <button class="btn btn-default" @click="turn(index)"><span class="glyphicon glyphicon-off"></span></button>
                        </th>
                        <th style="padding-left: 16px" class="smallest-column">
                            <button class="btn btn-default" @click="toggleRemoveServerModal(server, index)"><span class="glyphicon glyphicon-trash"></span></button>
                        </th>
                    </tr>
                </tbody>
            </table>
            <div v-else>
                You dont have any servers registered. Please, register them in the button below.
            </div>
        </div>

        <div class="box col-xs-8 col-xs-offset-2">
            <div style="margin-bottom: 25px; margin-top: 5px" class="col-xs-8">Number of graphs per line:</div>
            <div class="col-xs-4">
                <select class="form-control" v-model="configurations.graphsPerLine">
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                </select>
            </div>

            <div style="margin-bottom: 25px" class="col-xs-8">Period to analyze data (minutes):</div>
            <div class="col-xs-4">
                <input class="form-control" type="number" min="1" max="30" v-model="configurations.period"/>
            </div>

            <div style="margin-bottom: 25px" class="col-xs-8">Spacing between data (in number of values). For example, 3 means every 3 values in database we return 1:</div>
            <div class="col-xs-4">
                <input class="form-control" type="number" min="1" max="10" v-model="configurations.spacing"/>
            </div>

            <div style="margin-bottom: 25px" class="col-xs-8">Interval to get new data (seconds):</div>
            <div class="col-xs-4">
                <input class="form-control" type="number" min="1" max="30" v-model="configurations.interval"/>
            </div>

            <div style="margin-bottom: 25px" class="col-xs-8">Maximum number of points in each graph:</div>
            <div class="col-xs-4">
                <input class="form-control" type="number" min="2" max="1000" v-model="configurations.maxPoints"/>
            </div>

            <div style="margin-bottom: 25px" class="col-xs-8">Initialize with graphs expanded:</div>
            <div class="col-xs-4">
                <input class="form-control" type="checkbox" v-model="configurations.initializeExpanded"/>
            </div>
        </div>

        <div class="footer">
            <div align="center">
                <button @click="toggleNewServerModal(this)" class="btn btn-primary footer-btn"><span class="glyphicon glyphicon-plus"></span> Add Server</button>
            </div>
        </div>
    </div>
</template>

<script>
import NewServerModal from './NewServerModal';
import RemoveServerModal from './RemoveServerModal';

import { activateServer, deleteServer } from '../services/server';

export default {
    name: 'configurations',
    components: {
        NewServerModal,
        RemoveServerModal,
    },
    props: ['servers', 'configurations'],
    data() {
        return {
            showingNewServerModal: false,
            showingRemoveServerModal: false,
            removeIdx: -1,
        };
    },
    computed: {
        empty() {
            return !this.servers || !this.servers.length;
        },
    },
    methods: {
        success(msg) {
            this.$notify({ title: 'Success!', text: msg, type: 'success' });
        },
        error(msg) {
            this.$notify({ title: 'Error!', text: msg, type: 'error' });
        },
        turn(idx) {
            activateServer(this.servers[idx].name).then((res) => {
                console.log(res);
                this.$set(this.servers[idx], 'active', !this.servers[idx].active);
                this.success(`Server ${this.servers[idx].active ? 'de' : ''}activated succesfully!`);
            }).catch(() => {
                this.error(`Unable to ${this.servers[idx].active ? 'de' : ''}activate server!`);
            });
        },
        removeServer() {
            const idx = this.removeIdx;
            if (idx === -1) return;
            this.removeIdx = -1;
            deleteServer(this.servers[idx].name).then((res) => {
                console.log(res);
                this.servers.splice(idx, 1);
                this.success('Server removed succesfully!');
            }).catch((err) => {
                console.log(err);
                this.error('Unable to remove server. Try again later.');
            })
        },
        toggleNewServerModal(server) {
            if (this.showingNewServerModal) {
                this.$modal.hide('new-server-modal');
            } else {
                this.$modal.show('new-server-modal', server);
            }
            this.showingNewServerModal = !this.showingNewServerModal;
        },
        toggleRemoveServerModal(server, idx) {
            if (this.showingRemoveServerModal) {
                this.$modal.hide('remove-server-modal');
            } else {
                this.removeIdx = idx;
                this.$modal.show('remove-server-modal', server);
            }
            this.showingRemoveServerModal = !this.showingRemoveServerModal;
        },
    }
};
</script>

<style scoped>
.box {
    border: 1px solid #bababa;
    border-radius: 3px;
    padding-top: 25px;
    padding-bottom: 15px;
}
</style>