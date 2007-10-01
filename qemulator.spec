%if %mdkversion
%if %mdkversion < 200700
# default to non-modular X on MDV < 200700
%define _modular_X 0%{?_with_modular_x:1}
%else
# default to modular X on MDV >= 200700
%define _modular_X 0%{!?_without_modular_x:1}
%endif
%else
# default to modular X elsewhere
%define _modular_X 0%{!?_without_modular_x:1}
%endif

%define	name	qemulator
%define oname   Qemulator
%define	version	0.5
%define	release	%mkrel 1

Summary:	Interface to configure and launch Qemu
Name:		%name
Version:	%version
Release:	%release
License:	GPL
Group:		Emulators
URL:		http://qemulator.createweb.de/
Source0:	http://qemulator.createweb.de/%{oname}-%{version}.tar.gz
Patch0:         fix_python_dir.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	perl-Locale-gettext >= 1.04
Requires:       python
Requires:       pygtk2.0
Requires:       libglade2.0
Requires:       python-gnome
BuildRequires:	librsvg
BuildRequires:	libxml2-utils
BuildRequires:	desktop-file-utils
BuildRequires:  libglade2.0-devel
BuildRequires:  pygtk2.0-devel
BuildRequires:  python-gnome-devel

%if %_modular_X
BuildRequires:  x11-server-xvfb
%define _xvfb /usr/bin/Xvfb
%else
BuildRequires:  xorg-x11-Xvfb
%define _xvfb /usr/X11R6/bin/Xvfb
%endif

%description
A launcher for Qemu that manages Qemu configs and creates disk images
Qemu-launcher provides a point and click interface to Qemu. It also
allows you to create, save, load, and run multiple Qemu VM
configurations. It has a basic interface for creating or convertering
disk images.

Only supports the x86 PC emulator part of Qemu.

%prep
%setup -q -n %{oname}-%{version}

%patch0 -p1

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin \
         %{buildroot}/usr/share/ \
         %{buildroot}/usr/share/%{name} \
         %{buildroot}/usr/share/pixmaps \
         %{buildroot}/usr/lib
cp -a usr/local/lib/qemulator/* %{buildroot}/usr/share/qemulator
cp -ra usr/local/share/* %{buildroot}/usr/share/
chmod +x %{buildroot}/usr/share/qemulator/qml_imagecreation.py \
         %{buildroot}/usr/share/qemulator/qml_machinesetup.py \
         %{buildroot}/usr/share/qemulator/qml_filehandlers.py \
         %{buildroot}/usr/share/qemulator/qml_configuration.py \
         %{buildroot}/usr/share/qemulator/qml_tools.py \
         %{buildroot}/usr/share/qemulator/qml_installwizzard.py \
         %{buildroot}/usr/share/qemulator/qml_style.py
chmod -x %{buildroot}/usr/share/qemulator/icons/mac.png
convert -resize 32x32 usr/local/share/pixmaps/qemulator.svg qemulator.xpm
cp qemulator.xpm %{buildroot}/usr/share/pixmaps/
ln -s /usr/share/qemulator/qemulator.py %{buildroot}/usr/bin/qemulator

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/%name/*
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/pixmaps/%{name}/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/locale/*/LC_MESSAGES/%{oname}.mo
%{_datadir}/pixmaps/qemulator/*.png
