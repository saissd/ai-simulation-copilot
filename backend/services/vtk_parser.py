import pyvista as pv


def parse_vtk_file(file_path):
    try:
        mesh = pv.read(file_path)

        # ✅ Points
        points = mesh.points.tolist() if mesh.points is not None else []

        # ✅ Scalars (FIXED)
        scalar_names = []
        scalar_data = {}

        if mesh.point_data:
            for key in mesh.point_data:
                scalar_names.append(key)
                scalar_data[key] = mesh.point_data[key].tolist()

        # Preview points
        preview_points = points[:10] if points else []

        return {
            "points": points,
            "scalar_names": scalar_names,
            "scalar_data": scalar_data,
            "preview_points": preview_points
        }

    except Exception as e:
        print("VTK ERROR:", e)
        return {
            "points": [],
            "scalar_names": [],
            "scalar_data": {},
            "preview_points": []
        }


def summarize_simulation(parsed):
    num_points = len(parsed.get("points", []))
    num_scalars = len(parsed.get("scalar_names", []))

    summary = f"This simulation contains {num_points} points and {num_scalars} scalar fields."

    if parsed.get("scalar_names"):
        summary += f" Scalars include: {', '.join(parsed['scalar_names'])}."

    return summary