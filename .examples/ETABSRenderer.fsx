#I "/workspaces/Calcpad.Studio/projects"
#r "Calcpad.Studio.Interop.CSI/bin/Debug/net48/Calcpad.Studio.Interop.CSI.dll"

open System
open Calcpad.Studio.Interop.CSI
open Calcpad.Studio.Interop.CSI.IO
open Calcpad.Studio.Interop.CSI.Model
open Calcpad.Studio.Interop.CSI.Renderer


let app = ETABS.start ()
let workingDir = FileWatcher.queryWorkingDirectory ()

FileWatcher.create
    workingDir
    (FileWatcher.onChangeUpdateModel<BuildingBlueprint, Building>
        deserializeJson<BuildingBlueprint>
        validate
        (render app))

// Close ETABS instance.
Console.ReadKey() |> ignore
ETABS.close app DoNotSaveFile
